
org 100h


.data
stringa db "MAIUSCOLO A MINUSCOLO",0

.code
inizio:
mov ax, @data
mov ds, ax
mov si, offset stringa
; stampa la stringa originale
mov dx, offset stringa
mov ah, 09h
int 21h
; stampa una riga vuota
mov dl, 0dh
mov ah, 02h
int 21h
mov dl, 0ah
int 21h
ciclo:
mov al, [si]
cmp al, 'A'
jb fine
cmp al, 'Z'
jae ciclo2
add al, 32
mov [si], al
ciclo2:
cmp al, 'a'
jb fine
cmp al, 'z'
jae ciclo
sub al, 32
mov [si], al
jmp ciclo

fine:
;stampa la stringa modificata
mov dx, offset stringa
mov ah, 09h
int 21h
mov ax, 4c00h
int 21h
end inizio

ret