    global  _main
    extern  _printf
    extern  _scanf

    section .text

_main:
    push msg
    call _printf

    push value
    push input
    call _scanf

    push value
    push input
    call _printf

    ret

section .bss
    value: resb 1

section .data
    msg:   db    "Text input: ", 0
    input: db    "%s", 0
