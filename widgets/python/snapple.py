#!/usr/bin/env python3
"""
PyTermGUI Feature Lab

A single-file playground that hits a lot of PyTermGUI’s surface area:
- WindowManager + Layout
- Multiple Windows (draggable/resizable, scrollable)
- Containers / Splitters
- Labels, Buttons, InputField, Checkbox, Slider, Collapsible
- TIM markup, aliases, macros, #auto
- Palettes & boxes styling
- Animations (attr + float)
- Global keybindings

Run with:  python ptg_feature_lab.py
"""

import time
import pytermgui as ptg


# ---------------------------------------------------------------------------
# TIM setup: aliases & macros
# ---------------------------------------------------------------------------

def _macro_time(fmt: str) -> str:
    """TIM macro: [!time %c] -> formatted time string."""
    return time.strftime(fmt)


def configure_tim_and_palette() -> None:
    # Macro for live time display (used in header window)
    ptg.tim.define("!time", _macro_time)

    # Some style aliases (names are arbitrary)
    ptg.tim.alias("accent", "primary+1 bold")
    ptg.tim.alias("title", "accent #auto")
    ptg.tim.alias("muted", "surface+1 dim")
    ptg.tim.alias("danger", "red bold")

    # Background aliases (palette-based)
    ptg.tim.alias("@panel", "@surface+1")
    ptg.tim.alias("@panel-strong", "@surface+2")


# ---------------------------------------------------------------------------
# Global widget styling
# ---------------------------------------------------------------------------

def configure_global_styles() -> None:
    """Set some global styles / box chars so the app looks coherent."""
    # Use SINGLE box chars for all windows.
    ptg.boxes.SINGLE.set_chars_of(ptg.Window)

    # Make labels use TIM markup (already default), just here as example
    ptg.Label.set_style("value", "surface+1 #auto")

    # InputField prompt & cursor style demo
    ptg.InputField.set_style("prompt", "muted italic")
    ptg.InputField.set_style("cursor", "@primary+2")

    # Button style
    ptg.Button.set_style("label", "accent #auto")

    # Checkbox style
    ptg.Checkbox.set_style("label", "#auto")
    ptg.Checkbox.set_style("checkbox", "accent")

    # Collapsible header styling
    ptg.Collapsible.set_style("label", "accent")


# ---------------------------------------------------------------------------
# Demo windows
# ---------------------------------------------------------------------------

def make_header_window() -> ptg.Window:
    """Top banner window – shows time via TIM macro + basic markup."""
    header_text = (
        "[title]PyTermGUI Feature Lab[/]\n"
        "[muted]Drag, resize, press buttons, use keyboard. "
        "This is meant as a 'feature atlas', not a polished app.[/]\n\n"
        "[muted]Time:[/] [!time %c]"
    )
    win = ptg.Window(
        header_text,
        box="SINGLE",
        is_persistent=True,  # keep even if not focused
    )
    win.vertical_align = ptg.VerticalAlignment.TOP
    return win


def make_menu_window(manager: ptg.WindowManager) -> ptg.Window:
    """Sidebar window with buttons that spawn / focus other demos."""
    # Simple registry so we don't create duplicates
    windows_by_tag: dict[str, ptg.Window] = {}

    def open_or_focus(tag: str) -> None:
        # If we've created it before and it's still alive, just focus it
        wnd = windows_by_tag.get(tag)
        if wnd is not None:
            wnd.focus()
            return

        # Not found -> create a new one
        if tag == "widgets":
            wnd = make_widget_zoo_window()
        elif tag == "animations":
            wnd = make_animation_window()
        elif tag == "tim":
            wnd = make_tim_sandbox_window()
        else:
            return

        # Remember it and add to manager
        windows_by_tag[tag] = wnd
        manager.add(wnd)
        wnd.focus()

    btn_widgets = ptg.Container(
        "[title]Demos[/]",
        "",
        ptg.Button("Widget zoo",  lambda *_: open_or_focus("widgets")),
        ptg.Button("Animations",  lambda *_: open_or_focus("animations")),
        ptg.Button("TIM / styling", lambda *_: open_or_focus("tim")),
        "",
        ptg.Button("[danger]Quit (q)[/]", lambda *_: manager.stop()),
    )

    win = ptg.Window(btn_widgets, box="SINGLE", is_persistent=True)
    win.width = 30
    win.vertical_align = ptg.VerticalAlignment.TOP
    return win


def make_widget_zoo_window() -> ptg.Window:
    """Shows a bunch of builtin widgets and their interactions."""
    name_field = ptg.InputField(prompt="[muted]Name>[/] ")
    email_field = ptg.InputField(prompt="[muted]Email>[/] ")
    newsletter_chk = ptg.Checkbox("Subscribe to newsletter", value=True)

    # Create slider first, then set value AFTER __init__ so is_locked exists
    volume_slider = ptg.Slider()
    volume_slider.value = 0.3  # 0.0–1.0

    info_label = ptg.Label("[muted]Fill out the form and press Submit.[/]")

    def on_submit(*_) -> None:
        info_label.value = (
            "[accent]Submitted:[/]\n"
            f" - Name: [bold]{name_field.value or '<empty>'}[/]\n"
            f" - Email: [bold]{email_field.value or '<empty>'}[/]\n"
            f" - Newsletter: [bold]{'yes' if newsletter_chk.value else 'no'}[/]\n"
            f" - Volume: [bold]{int(volume_slider.value * 100)}[/]"
        )

    # Collapsible section
    collapsible = ptg.Collapsible(
        "Advanced options",
        ptg.Label("[muted]Imagine more controls here…[/]"),
        ptg.Checkbox("Enable experimental mode"),
        ptg.Checkbox("Log debug output"),
    )

    # Splitter demo (label on left, slider on right)
    volume_row = ptg.Splitter(
        ptg.Label("Volume:", parent_align=0),
        volume_slider,
    )

    root = ptg.Container(
        "[title]Widget zoo[/]",
        "",
        {"Name": [name_field]},      # auto syntax
        {"Email": [email_field]},    # auto syntax again
        "",
        newsletter_chk,
        "",
        volume_row,
        "",
        collapsible,
        "",
        ptg.Button("Submit", on_submit),
        "",
        "[muted]Tab/Shift+Tab moves focus. Space/Enter activates buttons.[/]",
        info_label,
    )

    win = ptg.Window(root, box="SINGLE", title="Widget zoo")
    win.overflow = ptg.Overflow.SCROLL
    win.vertical_align = ptg.VerticalAlignment.TOP
    win.width = 60
    win.height = 20
    return win


def make_animation_window() -> ptg.Window:
    """Demonstrate Animator, AttrAnimation and FloatAnimation."""
    animator = ptg.Animator()

    pulse_label = ptg.Label("[accent]Animating…[/]")
    float_label = ptg.Label("[muted]Float value: 0.0[/]")

    # We animate these attributes:
    pulse_label_alpha = {"value": 0.0}
    float_state = {"value": 0.0}

    def _update_pulse_label(label: ptg.Label, state: dict) -> None:
        phase = state["value"]
        style = "accent" if phase < 0.5 else "muted"
        label.value = f"[{style}]Animating… ({phase:0.2f})[/]"

    def _update_float_label(label: ptg.Label, state: dict, value: float) -> None:
        state["value"] = value
        label.value = f"[muted]Float value:[/] [accent]{state['value']:0.2f}[/]"

    def start_attr_animation(*_) -> None:
        animator.animate_attr(
            target=pulse_label_alpha,
            attr="value",
            start=0.0,
            end=1.0,
            duration=1.0,
            loop=True,
            direction=1,
            on_step=lambda anim: _update_pulse_label(pulse_label, pulse_label_alpha),
        )

    def start_float_animation(*_) -> None:
        animator.animate_float(
            start=float_state["value"],
            end=float_state["value"] + 10.0,
            duration=2.0,
            direction=1,
            on_step=lambda anim: _update_float_label(
                float_label, float_state, anim.value
            ),
        )

    controls = ptg.Container(
        ptg.Button("Start pulsing label", start_attr_animation),
        ptg.Button("Start float animation", start_float_animation),
        "",
        "[muted]Animations run via Animator.tick() each frame.[/]",
    )

    root = ptg.Container(
        "[title]Animations[/]",
        "",
        pulse_label,
        float_label,
        "",
        controls,
    )

    win = ptg.Window(root, box="SINGLE", title="Animations demo")
    win.width = 60
    win.height = 15

    # Tick animator each time the window is drawn
    _orig_get_lines = win.get_lines

    def _get_lines_hook() -> list[str]:
        animator.tick()
        return _orig_get_lines()

    win.get_lines = _get_lines_hook  # type: ignore[assignment]

    return win


def make_tim_sandbox_window() -> ptg.Window:
    """Window that shows TIM markup, aliases, macros, palette behavior."""
    examples = [
        "[accent]Accent text[/]",
        "[muted]Muted text[/]",
        "[danger]Danger text[/]",
        "",
        "[@panel #auto]Panel bg via @panel + #auto[/]",
        "[@panel-strong #auto]Stronger panel bg[/]",
        "",
        "[title]Hyperlink example:[/] [~https://github.com/bczsalba/pytermgui]"
        "PyTermGUI repo[/~]",
        "",
        "[muted]TIM macro time:[/] [!time %H:%M:%S]",
    ]

    tim_label = ptg.Label("\n".join(examples))

    help_text = ptg.Label(
        "[muted]"
        "This window is mostly about TIM / styling:\n"
        " - aliases: [accent], [muted], [danger], [title]\n"
        " - background aliases: [@panel], [@panel-strong]\n"
        " - #auto for readable foreground on any bg\n"
        " - macros: [!time %%H:%%M:%%S]\n"
        " - hyperlink syntax [~url]label[/~]\n"
        "[/]"
    )

    root = ptg.Container(
        "[title]TIM / styling demo[/]",
        "",
        tim_label,
        "",
        help_text,
    )

    win = ptg.Window(root, box="SINGLE", title="TIM / styling")
    win.width = 72
    win.height = 20
    win.overflow = ptg.Overflow.SCROLL
    return win


# ---------------------------------------------------------------------------
# Main app orchestration
# ---------------------------------------------------------------------------

def main() -> None:
    configure_tim_and_palette()
    configure_global_styles()

    with ptg.alt_buffer():
        with ptg.WindowManager() as manager:
            # Layout: header full-width, then sidebar + body.
            layout = ptg.Layout()
            layout.add_slot("header", height=3)
            layout.add_break()
            layout.add_slot("sidebar", width=0.23)
            layout.add_slot("body")
            manager.layout = layout

            # Global keybinding: q to quit
            manager.bind("q", lambda *_: manager.stop())

            # Create core windows
            header = make_header_window()
            sidebar = make_menu_window(manager)

            # Add to manager; it will place them according to layout slots
            manager.add(header, assign="header")
            manager.add(sidebar, assign="sidebar")

            # Body placeholder
            placeholder = ptg.Window(
                "[muted]Choose a demo from the left sidebar.[/]",
                box="SINGLE",
                title="Welcome",
            )
            manager.add(placeholder, assign="body")


if __name__ == "__main__":
    main()
