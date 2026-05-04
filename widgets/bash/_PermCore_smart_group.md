# PermCore Usage Documentation

PermCore is a state-driven Linux ownership, group, and permission manager.

```bash
alias PermCore="/opt/rightthumb-widgets-v0/widgets/bash/PermCore_smart_group.sh"
alias per="/opt/rightthumb-widgets-v0/widgets/bash/PermCore_smart_group.sh"
alias permcore="/opt/rightthumb-widgets-v0/widgets/bash/PermCore_smart_group.sh"
alias PC="/opt/rightthumb-widgets-v0/widgets/bash/PermCore_smart_group.sh"
alias .pc="/opt/rightthumb-widgets-v0/widgets/bash/PermCore_smart_group.sh"
```

It works in four phases:

1. load saved state first
2. apply command-line switches on top of loaded state
3. resolve and print the final plan
4. either save, print, or execute

That means what you see printed is the actual final merged state.

---

## Core ideas

PermCore stores settings in one master state object.

That state contains:

* single-value settings like owner, group, delay, profile
* list settings like users, paths, files, folders, excludes

The most important behavior is:

* `-load` happens first
* later switches override or extend what was loaded
* `-save` writes the final state and exits
* `-print` shows the final state and exits

---

## Main command patterns

### Add users to a group

```bash
permcore -g sds -u user1 user2
```

### Apply ownership/group/perms to paths

```bash
permcore -g sds -p /opt/app /home/user1/public_html
```

### Use automatic owner and group inference

```bash
permcore -o auto -g auto -p /home/user1/public_html
```

### Load a saved profile and run it

```bash
permcore -load /opt/base.permcore.json
```

### Load a saved profile and add more users

```bash
permcore -load /opt/base.permcore.json -u user3 user4
```

### Load a saved profile and add more paths

```bash
permcore -load /opt/base.permcore.json -p /opt/shared /var/www/html
```

### Save a new profile and quit

```bash
permcore -g sds -u user1 user2 -save /opt/sds.permcore.json
```

### Load, modify, save, and quit

```bash
permcore -load /opt/sds.permcore.json -g wheel -save /opt/wheel.permcore.json
```

### Print exactly what would happen and quit

```bash
permcore -load /opt/base.permcore.json -p /opt/app -print
```

---

## Command structure

### Single-value switches

These change one setting.

#### Owner

```bash
-o root
-owner root
-o auto
```

Sets the owner behavior.

* `root` means use that exact owner
* `auto` means try to infer owner from `/home/<user>/...`

#### Group

```bash
-g sds
-group sds
-g auto
```

Sets the group behavior.

* explicit group name uses that exact group
* `auto` tries to infer group from the path owner’s primary group

#### Delay

```bash
-delay 5
```

Used only in silent mode.

#### Directory mode

```bash
-dm 2770
-dir-mode 2770
```

Sets the chmod mode for directories.

#### File mode

```bash
-fm 660
-file-mode 660
```

Sets the chmod mode for files.

#### Clone source

```bash
-clone /path/to/reference
```

Copies settings from an existing file or folder into state.

#### Profiles

```bash
-web
-default
-x
-7
```

These apply preset permission mode patterns.

#### Fix exact 777

```bash
-777
```

Searches for exact `777` items under path targets and fixes them using the current settings.

---

### Multi-value switches

These can take one or more values.

#### Users

```bash
-u user1 user2
-users user1 user2
```

Adds users to the `users[]` list.

#### Paths

```bash
-p /opt/app /home/user1/public_html
-paths /opt/app /home/user1/public_html
```

Adds items to the `paths[]` list.

#### Files

```bash
-f file1.txt file2.php
-files file1.txt file2.php
```

Adds items to the `files[]` list.

#### Folders

```bash
-d folder1 folder2
-folders folder1 folder2
```

Adds items to the `folders[]` list.

#### Excludes

```bash
-e node_modules .git cache
-exclude node_modules .git cache
```

Adds items to the `excludes[]` list.

---

## Save, load, and print

### Load

```bash
-load /opt/profile.permcore.json
```

Loads the JSON file first, before any other output.

Anything later on the command line can change what was loaded.

Example:

```bash
permcore -load /opt/base.permcore.json -g wheel -u user3
```

This means:

* load base config
* change group to `wheel`
* add `user3`

### Save

```bash
-save /opt/profile.permcore.json
```

Saves the final resolved state as JSON and exits.

It does **not** execute changes.

Example:

```bash
permcore -g sds -u user1 user2 -save /opt/sds.permcore.json
```

This writes the config only.

### Print

```bash
-print
```

Prints the final resolved plan and exits.

It never executes and is never saved as part of config.

Example:

```bash
permcore -load /opt/base.permcore.json -p /opt/newpath -print
```

---

## Behavior switches

### Silent

```bash
-silent
```

No prompts, but shows a countdown before execution.

### Force

```bash
-force
```

No prompts and no countdown.

### Dry run

```bash
-dry-run
```

Prints commands that would run without executing them.

### Verbose

```bash
-verbose
```

Shows more detail during execution.

### No recursive

```bash
-no-recursive
```

Do not recurse into directory trees for normal path operations.

### Follow symlinks

```bash
-follow-symlinks
```

Allows traversal through symlinks.

### Allow top

```bash
-allow-top
```

Allows dangerous recursive targets like `/home` or `/var`.

Without this, top-level targets are blocked for safety.

---

## Profiles

### `-web`

Sets:

* dirs = `755`
* files = `644`

Typical use:

```bash
permcore -web -o auto -g auto -p /home/user1/public_html
```

### `-default`

Sets:

* dirs = `2770`
* files = `660`

Typical use:

```bash
permcore -default -g sds -p /opt/shared
```

### `-x`

Sets:

* dirs = `755`
* files = `755`

Typical use:

```bash
permcore -x -g sds -p /opt/scripts
```

### `-7`

Sets:

* dirs = `777`
* files = `777`

Mostly for testing, not recommended for production.

---

## Automatic owner and group resolution

### Owner auto

```bash
-o auto
```

If a target path is under:

```bash
/home/<user>/...
```

and `<user>` exists, owner resolves to that user.

If owner cannot be inferred:

* interactive mode may ask for fallback
* non-interactive mode leaves owner unchanged unless fallback already exists in loaded state

### Group auto

```bash
-g auto
```

If owner can be inferred, group becomes that user’s primary group.

If group cannot be inferred:

* interactive mode may ask for fallback
* non-interactive mode leaves group unchanged unless fallback already exists in loaded state

---

## Effective target behavior

PermCore merges these into one effective target set:

* `paths[]`
* `files[]`
* `folders[]`

That means all of these become path targets for execution:

```bash
permcore -p /opt/app -f index.php -d storage
```

Internally the effective targets are:

* `/opt/app`
* `index.php`
* `storage`

Duplicates are removed automatically.

---

## User operations

User operations require an explicit group.

Valid:

```bash
permcore -g sds -u user1 user2
```

Invalid:

```bash
permcore -u user1 user2
permcore -g auto -u user1
```

For users, PermCore:

* checks each user exists
* creates the group if needed
* adds user to the group only if not already present

---

## Path operations

Path operations apply:

* owner, if resolved
* group, if resolved
* file mode, if configured
* dir mode, if configured

### Example

```bash
permcore -o root -g sds -dm 2770 -fm 660 -p /opt/shared
```

This applies:

* owner = root
* group = sds
* dirs = 2770
* files = 660

---

## Exact 777 fix mode

```bash
permcore -777 -g sds -default -p /opt/shared
```

This means:

* search under `/opt/shared`
* find files and directories with exact mode `777`
* fix them using current state

If no paths are provided, it defaults to:

```bash
.
```

---

## Inspection commands

### List users

```bash
permcore -list-users
```

### List groups

```bash
permcore -list-groups
```

### List users and their groups

```bash
permcore -list-users-groups
```

### List members of one group

```bash
permcore -list-group sds
```

### Show one path

```bash
permcore -folder /opt/shared
```

### Show one folder and immediate children

```bash
permcore -folder-files /opt/shared
```

---

## Save/load workflow examples

### Example 1: save a user-group profile

```bash
permcore -g sds -u user1 user2 -save /opt/sds.permcore.json
```

Later:

```bash
permcore -load /opt/sds.permcore.json
```

### Example 2: save common path settings

```bash
permcore -g sds -o auto -default -save /opt/commonPathSettings.permcore.json
```

Later:

```bash
permcore -load /opt/commonPathSettings.permcore.json -p /home/user1/public_html
```

### Example 3: load, modify, print

```bash
permcore -load /opt/commonPathSettings.permcore.json -g wheel -p /opt/shared -print
```

### Example 4: clone from a live path, then save

```bash
permcore -clone /home/user1/public_html -save /opt/webclone.permcore.json
```

---

## Alias examples

### Main alias

```bash
alias per="/opt/rightthumb-widgets-v0/widgets/bash/PermCore_smart_group.sh"
```

### Path alias

```bash
alias pc.p="/opt/rightthumb-widgets-v0/widgets/bash/PermCore_smart_group.sh -load /opt/commonPathSettings.permcore.json -p"
```

Usage:

```bash
pc.p .
pc.p /home/user1/public_html
```

### User alias

```bash
alias pc.u="/opt/rightthumb-widgets-v0/widgets/bash/PermCore_smart_group.sh -load /opt/sds.permcore.json -u"
```

Usage:

```bash
pc.u user1 user2
```

---

## Recommended safe workflow

### See what a command would do

```bash
permcore -load /opt/base.permcore.json -p /opt/shared -print
```

### Show commands without running them

```bash
permcore -load /opt/base.permcore.json -p /opt/shared -dry-run
```

### Save a modified profile

```bash
permcore -load /opt/base.permcore.json -g wheel -save /opt/wheel.permcore.json
```

### Execute for real

```bash
permcore -load /opt/wheel.permcore.json -p /opt/shared
```

---

## Notes for automation

### Cron-safe printless execution

```bash
permcore -load /opt/job.permcore.json -force
```

### Safer non-interactive execution

```bash
permcore -load /opt/job.permcore.json -silent -delay 5
```

### Cron-safe state creation

```bash
permcore -o auto -g auto -default -p /home/user1/public_html /opt/shared -save /opt/job.permcore.json
```

Then in cron:

```bash
* * * * * /opt/rightthumb-widgets-v0/widgets/bash/PermCore_smart_group.sh -load /opt/job.permcore.json -force
```

---

## Switch precedence rules

PermCore resolves state like this:

1. built-in defaults
2. loaded JSON profile
3. later command-line switches
4. runtime auto-resolution for owner/group per path
5. print, save, or execute

So this:

```bash
permcore -load /opt/base.permcore.json -g wheel -u user3
```

means:

* start with defaults
* load base file
* set group to `wheel`
* add `user3`

The printed plan reflects that final merged result.

---

## What gets saved

Saved JSON includes:

* all scalar settings
* all list settings
* current resolved switch state

It does **not** save the ephemeral command intent of `-print`.

`-save` always writes JSON and exits.

---

## Common mistakes

### Saving and expecting execution

```bash
permcore -g sds -u user1 user2 -save /opt/test.json
```

This saves only. It does not execute.

### Using user operations with `-g auto`

```bash
permcore -g auto -u user1
```

This is invalid. User operations need an explicit group.

### Forgetting `-print`

If you want to inspect a loaded/modified state without running anything:

```bash
permcore -load /opt/base.permcore.json -p /opt/shared -print
```

---

## Suggested help summary for daily use

```bash
permcore -load profile.json -print
permcore -load profile.json -save new.json
permcore -load profile.json -p /path1 /path2
permcore -g sds -u user1 user2
permcore -o auto -g auto -default -p /home/user1/public_html
permcore -777 -g sds -default -p /opt/shared
```

If you want, I can turn this into a polished markdown README with sections for installation, examples, JSON format, and troubleshooting.