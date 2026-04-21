import os
import time

class Meta_Namespace:
    def __init__(self):
        pass

dot = Meta_Namespace  # your pattern
def addComma(n): return f"{n:,}"




def walk_fs(root='.', recursive=True):
    root = os.path.abspath(root)

    for dirpath, dirnames, filenames in os.walk(root):
        # folders
        for name in dirnames:
            # print(10001)
            path = os.path.join(dirpath, name)
            r.iter.folders += 1
            yield {
                "type": "folder",
                "path": path,
                "relative": safe_relpath(path, root),
            }

        # files
        for name in filenames:
            path = os.path.join(dirpath, name)
            # print(path)

            r.iter.files += 1
            yield {
                "type": "file",
                "path": path,
                "relative": safe_relpath(path, root),
            }

        if not recursive:
            break




def safe_relpath(path, start):
    try:
        return os.path.relpath(path, start)
    except ValueError:
        # Different drive/mount (ex: \\.\nul vs D:)
        return path


def is_reparse_point(entry):
    try:
        return entry.is_symlink()
    except OSError:
        return True







import os
import stat
import time

def file_meta(path, key):
    """
    Get a specific piece of file metadata.

    path : file path
    key  : metadata key (string)

    Supported keys:
        size
        atime / mtime / ctime
        mode
        inode
        device
        nlink
        uid / gid
        is_file / is_dir / is_link
    """
    st = os.stat(path, follow_symlinks=False)

    meta = {
        "size": st.st_size,

        "atime": st.st_atime,
        "mtime": st.st_mtime,
        "ctime": st.st_ctime,

        "atime_iso": time.ctime(st.st_atime),
        "mtime_iso": time.ctime(st.st_mtime),
        "ctime_iso": time.ctime(st.st_ctime),

        "mode": stat.filemode(st.st_mode),
        "inode": st.st_ino,
        "device": st.st_dev,
        "nlink": st.st_nlink,
        "uid": st.st_uid,
        "gid": st.st_gid,

        "is_file": stat.S_ISREG(st.st_mode),
        "is_dir": stat.S_ISDIR(st.st_mode),
        "is_link": stat.S_ISLNK(st.st_mode),
    }

    return meta.get(key)





# import _rightThumb._dir as _dir


run = dot()
r = dot()

def action():
    r.start = time.time()
    r.iter = dot()
    r.iter.files = 0
    r.iter.folders = 0

    # IMPORTANT: you must iterate the generator or nothing happens
    for fsObject in walk_fs(root='.', recursive=True):
        pass
        for x in dir(fsObject):
            print(x)
        return

        # or test your registry hook here:
        # registry.dispatch("fsObject", fsObject)

    r.end = time.time()
    r.diff = r.end - r.start
    print(f"Walked filesystem in {r.diff:.2f} seconds, found {r.iter.files:,} files and {r.iter.folders} folders.")

if __name__ == "__main__":
    action()