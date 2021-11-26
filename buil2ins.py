import builtins

# Step -1: Settings
buil2ins_try = []
buil2ins_must = ["int"]

# Step 0: Setup
buil2ins_done = []

# Step 1: get all the maybe builtins and put them in this buil2ins.py
for buil2in in buil2ins_try:
    try:
        exec("global {0};{0} = builtins.{0}".format(buil2in))
        buil2ins_done.append(buil2in)
    except Exception:
        pass

# Step 2: get the mandatory builtins
for buil2in in buil2ins_must:
    try:
        exec("global {0};{0} = builtins.{0}".format(buil2in))
        buil2ins_done.append(buil2in)
    except Exception as e:
        raise Exception(f"unable to get a needed builtin ({buil2in})") from e

# Step 3: put in __all__
__all__ = buil2ins_done
