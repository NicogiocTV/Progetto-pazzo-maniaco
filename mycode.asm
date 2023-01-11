
org 100h


.data
stringa db "MAIUSCOLO A MINUSCOLO",0

.code
inizio:
mov ax, @data
mov ds, ax
mov si, offset stringa
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
mov ax, 4c00h
int 21h
end inizio

ret