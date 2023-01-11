
org 100h
    
    MOV AH,09
    LEA DX,string
    INT 21h

    
; ciclo per ogni carattere
ciclo:
    mov al, [si]
    cmp al, 'A'
    jb not_upper
    cmp al, 'Z'
    ja not_upper

    ; trasforma il carattere in minuscolo
    MOV AH,02
    add al, 20
    mov [si], al
    int 21h

not_upper:
    inc si
    loop ciclo

; Exit program
    MOV AH,02
    mov ax, 4c00h
    int 21h

;    section .data
    string db 'AsDfGhJjjkq$'

ret




