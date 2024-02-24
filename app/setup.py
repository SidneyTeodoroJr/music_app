from cx_Freeze import setup, Executable

# Configurando o projeto
build_exe_options = {
    "packages": ["flet"],  # Dependências
}

# Configuração do executável (APP)
setup(
    name="MusicAPP",\
    version="1.0",
    description="Um projeto simples de aplicativo desenvolvido usando a biblioteca Python Flet.",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base="Win32GUI")]  # Sem o terminal de comando `base="Win32GUI"`
                                                          # Com o Terminal `base=None`
)