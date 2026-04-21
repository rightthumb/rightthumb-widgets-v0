from __future__ import annotations

'''
from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator
from prompt_toolkit.shortcuts import checkboxlist_dialog, radiolist_dialog

email_validator = Validator.from_callable(
    lambda t: "@" in t,
    error_message="Invalid email",
    move_cursor_to_end=True,
)

name = prompt("Name: ")
email = prompt("Email: ", validator=email_validator)
notes = prompt("Notes: ")

options = checkboxlist_dialog(
    title="Options",
    text="Select features",
    values=[
        ("logging", "Enable logging"),
        ("backup", "Enable backups"),
        ("debug", "Debug mode"),
    ],
).run()

priority = radiolist_dialog(
    title="Priority",
    text="Select priority",
    values=[
        ("low", "Low"),
        ("med", "Medium"),
        ("high", "High"),
    ],
).run()

data = {
    "name": name,
    "email": email,
    "notes": notes,
    "options": options,
    "priority": priority,
}

print(data)

'''



'''
from textual.app import App
from textual.widgets import Input, Button, Label

class FormApp(App):

    def compose(self):
        yield Label("Name")
        self.name_input = Input()
        yield self.name_input

        yield Label("Email")
        self.email_input = Input()
        yield self.email_input

        yield Button("Submit", id="submit")

    def on_button_pressed(self, event):
        if event.button.id == "submit":
            data = {
                "name": self.name_input.value,
                "email": self.email_input.value,
            }
            self.exit(data)

result = FormApp().run()
print(result)
'''








# textual_complex_form.pyfrom __future__ import annotations

import re
from dataclasses import dataclass, asdict
from datetime import datetime

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.reactive import reactive
from textual.screen import ModalScreen
from textual import events
from textual.widgets import (
    Button,
    DataTable,
    Footer,
    Header,
    Input,
    Label,
    Markdown,
    Static,
    Switch,
    TabbedContent,
    TabPane,
    TextArea,
)

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
IPV4_RE = re.compile(
    r"^(?:(?:25[0-5]|2[0-4]\d|1?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|1?\d?\d)(?:/\d{1,2})?$"
)


def is_email(s: str) -> bool:
    return bool(EMAIL_RE.match(s.strip()))


def is_ipv4_or_cidr(s: str) -> bool:
    s = s.strip()
    if not s:
        return True  # allow blank
    if not IPV4_RE.match(s):
        return False
    if "/" in s:
        try:
            bits = int(s.split("/", 1)[1])
            return 0 <= bits <= 32
        except ValueError:
            return False
    return True


@dataclass
class Record:
    customer: str = ""
    email: str = ""
    active: bool = True
    plan: str = "Standard"
    ip: str = ""
    gateway: str = ""
    dns: str = "1.1.1.1, 8.8.8.8"
    notes: str = ""


class Confirm(ModalScreen[bool]):
    """A simple yes/no modal that returns True/False."""

    BINDINGS = [
        ("escape", "no", "Cancel"),
        ("y", "yes", "Yes"),
        ("n", "no", "No"),
        ("enter", "yes", "Yes"),
    ]

    def __init__(self, title: str, body: str) -> None:
        super().__init__()
        self._title = title
        self._body = body

    def compose(self) -> ComposeResult:
        yield Container(
            Static(self._title, classes="confirm_title"),
            Static(self._body, classes="confirm_body"),
            Horizontal(
                Button("No", id="no"),
                Button("Yes", id="yes", variant="error"),
                classes="confirm_buttons",
            ),
            classes="confirm_modal",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss(event.button.id == "yes")

    def action_yes(self) -> None:
        self.dismiss(True)

    def action_no(self) -> None:
        self.dismiss(False)


class StatusBar(Static):
    """Bottom status line that updates from app state."""

    status = reactive("Ready")

    def watch_status(self, value: str) -> None:
        self.update(value)


class ComplexFormApp(App[None]):
    TITLE = "Textual Complex Form Example"

    CSS = """
    Screen { background: #0f111a; }
    #root { height: 100%; }

    /* left nav */
    #sidebar {
        width: 30;
        border: tall #2a2f45;
        padding: 1;
        background: #101322;
    }
    #sidebar Label.title { text-style: bold; margin-bottom: 1; }
    .navbtn { width: 100%; margin-bottom: 1; }
    .hint { color: #9aa4c7; margin-top: 1; }

    /* main */
    #main {
        border: tall #2a2f45;
        background: #0f111a;
        padding: 1;
    }

    /* form layout */
    .row { height: auto; margin-bottom: 1; }
    .field_label { width: 16; color: #c7cde8; }
    .field_box { width: 1fr; }

    Input.-invalid { border: tall #ff4d4d; }

    #preview_box {
        border: tall #2a2f45;
        padding: 1;
        height: 16;
        margin-top: 1;
    }

    #notes_area {
        height: 12;
        border: tall #2a2f45;
        padding: 1;
    }

    #notes_md {
        border: tall #2a2f45;
        padding: 1;
        height: 12;
        margin-top: 1;
    }

    /* modal */
    .confirm_modal {
        width: 70;
        height: auto;
        padding: 1 2;
        border: tall #2a2f45;
        background: #101322;
    }
    .confirm_title { text-style: bold; margin-bottom: 1; }
    .confirm_body { margin-bottom: 1; }
    .confirm_buttons { height: auto; }
    .confirm_buttons Button { margin-right: 2; }

    /* status */
    #status {
        dock: bottom;
        height: 1;
        padding-left: 1;
        background: #101322;
        color: #c7cde8;
    }
    """

    BINDINGS = [
        ("f2", "save", "Save"),
        ("f4", "reset", "Reset"),
        ("ctrl+p", "toggle_preview", "Preview"),
        ("ctrl+q", "quit_app", "Quit"),
    ]

    record: Record = Record()
    dirty: bool = reactive(False)
    show_preview: bool = reactive(True)

    def _row(self, label: str, widget, required: bool = False) -> Horizontal:
        widget.add_class("field_box")
        return Horizontal(
            Label(f"{label}{' *' if required else ''}", classes="field_label"),
            widget,
            classes="row",
        )

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)

        with Horizontal(id="root"):
            # Sidebar
            with Vertical(id="sidebar"):
                yield Label("Navigator", classes="title")
                yield Button("New Record", id="nav_new", classes="navbtn")
                yield Button("Load Sample", id="nav_sample", classes="navbtn")
                yield Button("Help / Keys", id="nav_help", classes="navbtn")
                yield Static("F2 Save • F4 Reset • Ctrl+P Preview • Ctrl+Q Quit", classes="hint")

            # Main
            with Vertical(id="main"):
                yield Label("Customer Provisioning Form", classes="title")

                with TabbedContent(id="tabs"):
                    with TabPane("General", id="tab_general"):
                        yield self._row("Customer", Input(placeholder="Jane Doe", id="customer"), required=True)
                        yield self._row("Email", Input(placeholder="jane@example.com", id="email"))

                        with Horizontal(classes="row"):
                            yield Label("Active", classes="field_label")
                            yield Switch(value=True, id="active")

                        yield self._row("Plan", Input(value="Standard", id="plan"))

                    with TabPane("Network", id="tab_network"):
                        yield self._row("IP", Input(placeholder="40.160.53.101/24", id="ip"))
                        yield self._row("Gateway", Input(placeholder="40.160.53.254", id="gateway"))
                        yield self._row("DNS", Input(value="1.1.1.1, 8.8.8.8", id="dns"))

                    with TabPane("Notes", id="tab_notes"):
                        yield Label("Notes (multi-line) -> Markdown preview", classes="hint")
                        yield TextArea("", id="notes_area")
                        yield Markdown("", id="notes_md")

                with Horizontal(classes="row"):
                    yield Button("Save", id="save", variant="success")
                    yield Button("Reset", id="reset", variant="warning")
                    yield Button("Toggle Preview", id="toggle_preview", variant="default")

                with Container(id="preview_box"):
                    yield Label("Live Preview", classes="title")
                    table = DataTable(id="preview_table")
                    table.add_columns("Field", "Value")
                    yield table
                    yield Static("", id="meta")

        yield StatusBar(id="status")
        yield Footer()

    def on_mount(self) -> None:
        # Delay until widget tree is fully available (esp. tabs)
        self.call_after_refresh(self._sync_ui_from_record)
        self.call_after_refresh(self._refresh_preview)
        self._status("Ready.")

    # ---------- helpers ----------
    def _status(self, msg: str) -> None:
        dirty_flag = " • UNSAVED" if self.dirty else ""
        self.query_one(StatusBar).status = f"{msg}{dirty_flag}"

    def _set_invalid(self, input_id: str, invalid: bool) -> None:
        w = self.query_one(f"#{input_id}", Input)
        if invalid:
            w.add_class("-invalid")
        else:
            w.remove_class("-invalid")

    def _read_ui_into_record(self) -> Record:
        return Record(
            customer=self.query_one("#customer", Input).value.strip(),
            email=self.query_one("#email", Input).value.strip(),
            active=self.query_one("#active", Switch).value,
            plan=self.query_one("#plan", Input).value.strip() or "Standard",
            ip=self.query_one("#ip", Input).value.strip(),
            gateway=self.query_one("#gateway", Input).value.strip(),
            dns=self.query_one("#dns", Input).value.strip(),
            notes=self.query_one("#notes_area", TextArea).text,
        )

    def _sync_ui_from_record(self) -> None:
        r = self.record
        self.query_one("#customer", Input).value = r.customer
        self.query_one("#email", Input).value = r.email
        self.query_one("#active", Switch).value = r.active
        self.query_one("#plan", Input).value = r.plan
        self.query_one("#ip", Input).value = r.ip
        self.query_one("#gateway", Input).value = r.gateway
        self.query_one("#dns", Input).value = r.dns

        self.query_one("#notes_area", TextArea).load_text(r.notes or "")
        self.query_one("#notes_md", Markdown).update(r.notes or "_(no notes)_")

    def _validate(self, r: Record) -> tuple[bool, str]:
        ok = True
        problems: list[str] = []

        if not r.customer:
            ok = False
            problems.append("Customer is required.")
            self._set_invalid("customer", True)
        else:
            self._set_invalid("customer", False)

        if r.email and not is_email(r.email):
            ok = False
            problems.append("Email looks invalid.")
            self._set_invalid("email", True)
        else:
            self._set_invalid("email", False)

        if not is_ipv4_or_cidr(r.ip):
            ok = False
            problems.append("IP must be IPv4 or CIDR (e.g. 1.2.3.4 or 1.2.3.4/24).")
            self._set_invalid("ip", True)
        else:
            self._set_invalid("ip", False)

        if r.gateway and not is_ipv4_or_cidr(r.gateway):
            ok = False
            problems.append("Gateway must be IPv4 (CIDR optional but unusual).")
            self._set_invalid("gateway", True)
        else:
            self._set_invalid("gateway", False)

        return ok, "\n".join(problems)

    def _refresh_preview(self) -> None:
        table = self.query_one("#preview_table", DataTable)
        table.clear()

        if not self.show_preview:
            self.query_one("#preview_box").display = False
            return

        self.query_one("#preview_box").display = True
        r = self._read_ui_into_record()

        for k, v in asdict(r).items():
            table.add_row(k, str(v))

        self.query_one("#meta", Static).update(
            f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )

        self.query_one("#notes_md", Markdown).update(r.notes or "_(no notes)_")

    async def _confirm_if_dirty(self, message: str) -> bool:
        if not self.dirty:
            return True
        return await self.push_screen_wait(Confirm("Unsaved Changes", message))

    # ---------- events ----------
    def on_input_changed(self, event: Input.Changed) -> None:
        self.dirty = True
        self._refresh_preview()
        self._status("Editing…")

    def on_switch_changed(self, event: Switch.Changed) -> None:
        self.dirty = True
        self._refresh_preview()
        self._status("Editing…")

    def on_text_area_changed(self, event: TextArea.Changed) -> None:
        if event.text_area.id == "notes_area":
            self.dirty = True
            self.query_one("#notes_md", Markdown).update(event.text_area.text or "_(no notes)_")
            self._refresh_preview()
            self._status("Editing…")

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        bid = event.button.id
        if bid == "nav_new":
            await self.action_reset()
        elif bid == "nav_sample":
            self._load_sample()
        elif bid == "nav_help":
            self.notify("F2 Save • F4 Reset • Ctrl+P Preview • Ctrl+Q Quit", title="Help", severity="information")
        elif bid == "save":
            await self.action_save()
        elif bid == "reset":
            await self.action_reset()
        elif bid == "toggle_preview":
            await self.action_toggle_preview()

    def _load_sample(self) -> None:
        self.record = Record(
            customer="Scott Reph",
            email="scott@example.com",
            active=True,
            plan="Pro",
            ip="40.160.53.101/24",
            gateway="40.160.53.254",
            dns="1.1.1.1, 8.8.8.8",
            notes="## Install Notes\n- Verify signal at **ground block**\n- If modem fails, check upstream levels\n",
        )
        self._sync_ui_from_record()
        self.dirty = False
        self._refresh_preview()
        self._status("Loaded sample record.")

    # ---------- actions ----------
    async def action_save(self) -> None:
        r = self._read_ui_into_record()
        ok, msg = self._validate(r)
        if not ok:
            self.notify(msg, title="Validation failed", severity="error")
            self._status("Fix validation errors.")
            return

        self.record = r
        self.dirty = False
        self._refresh_preview()
        self.notify("Saved.", title="Success", severity="information")
        self._status("Saved.")

    async def action_reset(self) -> None:
        if not await self._confirm_if_dirty("Reset form and lose changes?"):
            self._status("Reset canceled.")
            return
        self.record = Record()
        self._sync_ui_from_record()
        self.dirty = False
        self._refresh_preview()
        self._status("Reset to blank record.")

    async def action_toggle_preview(self) -> None:
        self.show_preview = not self.show_preview
        self._refresh_preview()
        self._status("Preview toggled.")

    async def action_quit_app(self) -> None:
        if not await self._confirm_if_dirty("Quit and lose unsaved changes?"):
            self._status("Quit canceled.")
            return
        self.exit()

    async def on_key(self, event: events.Key) -> None:
        if event.key == "tab":
            return




def scan_callable_paths(args):
    """
    Wrapper around scan_callables that returns only path strings.
    """
    rows = scan_callables({
        "target": args["target"],
        "name": args.get("name"),
        "max_depth": args.get("max_depth", 3),
        "include_private": args.get("include_private", False),
        "include_dunder": args.get("include_dunder", False),
        "include_classes": args.get("include_classes", True),
        "include_modules": args.get("include_modules", True),
        "show_signature": False,
        "print": False,
        "return": True,
    })
    result = [row["path"] for row in rows]
    if args.get("print", True):
        for item in result:
            print(item)
    return result


def scan_callables(args):
    """
    Recursively scan a module/object and collect callable namespaces.

    Single-dict args only.

    Args:
        {
            "target": module_or_object,          # required
            "name": "ffmpeg",                    # optional root label
            "max_depth": 3,                      # optional
            "depth": 0,                          # internal/start depth
            "include_private": False,            # optional
            "include_dunder": False,             # optional
            "include_classes": True,             # optional
            "include_modules": True,             # optional
            "show_signature": True,              # optional
            "print": True,                       # optional
            "return": True,                      # optional
            "seen": None,                        # internal
            "sort": True                         # optional
        }

    Returns:
        list[dict]
    """
    import inspect
    import types

    target = args.get("target")
    if target is None:
        raise ValueError("scan_callables requires args['target']")

    root_name = args.get("name", getattr(target, "__name__", "root"))
    max_depth = int(args.get("max_depth", 3))
    depth = int(args.get("depth", 0))
    include_private = bool(args.get("include_private", False))
    include_dunder = bool(args.get("include_dunder", False))
    include_classes = bool(args.get("include_classes", True))
    include_modules = bool(args.get("include_modules", True))
    show_signature = bool(args.get("show_signature", True))
    do_print = bool(args.get("print", True))
    do_return = bool(args.get("return", True))
    sort_items = bool(args.get("sort", True))

    seen = args.get("seen")
    if seen is None:
        seen = set()

    records = []

    def allowed_name(name):
        if name.startswith("__") and name.endswith("__"):
            return include_dunder
        if name.startswith("_"):
            return include_private
        return True

    def safe_signature(obj):
        try:
            return str(inspect.signature(obj))
        except Exception:
            return None

    def walk(obj, path, current_depth):
        obj_id = id(obj)
        if obj_id in seen:
            return
        seen.add(obj_id)

        if current_depth > max_depth:
            return

        try:
            names = dir(obj)
        except Exception:
            return

        if sort_items:
            names = sorted(names)

        for name in names:
            if not allowed_name(name):
                continue

            try:
                child = getattr(obj, name)
            except Exception:
                continue

            child_path = f"{path}.{name}"

            is_mod = inspect.ismodule(child)
            is_cls = inspect.isclass(child)
            is_call = callable(child)

            record = None

            if is_call:
                if is_cls and not include_classes:
                    pass
                else:
                    record = {
                        "path": child_path,
                        "name": name,
                        "depth": current_depth + 1,
                        "kind": (
                            "class" if is_cls else
                            "module" if is_mod else
                            "callable"
                        ),
                        "signature": safe_signature(child) if show_signature else None,
                        "object": child,
                    }
                    records.append(record)

                    if do_print:
                        sig = record["signature"] if record["signature"] else ""
                        if sig:
                            print(f"{record['depth']:>2}  {record['kind']:<8}  {child_path}{sig}")
                        else:
                            print(f"{record['depth']:>2}  {record['kind']:<8}  {child_path}")

            should_recurse = False

            if current_depth + 1 <= max_depth:
                if is_mod and include_modules:
                    should_recurse = True
                elif is_cls:
                    should_recurse = True
                elif hasattr(child, "__dict__") and not isinstance(child, (str, bytes, int, float, bool, list, tuple, dict, set)):
                    should_recurse = True

            if should_recurse:
                walk(child, child_path, current_depth + 1)

    walk(target, root_name, depth)

    if do_return:
        return records
    return []

def runScan(name, max_depth=2):
    paths = scan_callable_paths({
        "target": eval(name),
        "name": name,
        "max_depth": max_depth,
        "print": False,
    })
    return paths

import textual
paths = runScan("textual")
for path in paths:
    if not any(x in path for x in '.os. .sys. .utils. subprocess platform .re. .decorators. .Path.'.split()):
        if not '.os' in path:
            print(path)

# if __name__ == "__main__":
#     ComplexFormApp().run()
