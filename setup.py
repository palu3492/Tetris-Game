import cx_Freeze

executables = [cx_Freeze.Executable("tetris.py")]

cx_Freeze.setup(
    name="TETRIS",
    version = "1.2",
    options={"build_exe":{"packages":["random", "time", "pygame"],
                          "include_files":["files/"]}},
    executables = executables
    
    )
