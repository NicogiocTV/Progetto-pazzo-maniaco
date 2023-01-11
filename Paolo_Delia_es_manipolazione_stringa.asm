org 100h
        
MOV AH,09
LEA DX,mess
INT 21h

MOV AH,02
MOV DL,0Ah   ;a capo
INT 21h
MOV DL,0Dh   ;inizio riga
INT 21h
        
    ; stampa dei caratteri a capo e inizio linea
MOV AH,02
MOV DL,0Ah ;a capo
INT 21h
MOV DL,0Dh ;inizio riga
INT 21h

mov bl,mess[0]; carico il primo carattere sul reistro Bl
or bl,1100001b;carichiamo il valore della lettere minuscola in binario

mov mess[0],bl

mov bl,mess[1]; carico il secondo carattere sul reistro Bl
and bl,1010011b;carichiamo il valore della lettere minuscola in binario

mov mess[1],bl

mov bl,mess[2]; carico il primo carattere sul reistro Bl
or bl,1100100b;carichiamo il valore della lettere minuscola in binario

mov mess[2],bl

mov bl,mess[3]; carico il primo carattere sul reistro Bl
and bl,1000110b;carichiamo il valore della lettere minuscola in binario

mov mess[3],bl

mov bl,mess[4]; carico il primo carattere sul reistro Bl
or bl,1100111b;carichiamo il valore della lettere minuscola in binario

mov mess[4],bl

mov bl,mess[5]; carico il primo carattere sul reistro Bl
and bl,1001000b;carichiamo il valore della lettere minuscola in binario

mov mess[5],bl

mov bl,mess[6]; carico il primo carattere sul reistro Bl
or bl,1101010b;carichiamo il valore della lettere minuscola in binario

mov mess[6],bl

mov bl,mess[7]; carico il primo carattere sul reistro Bl
and bl,1001010b;carichiamo il valore della lettere minuscola in binario

mov mess[7],bl

mov bl,mess[8]; carico il primo carattere sul reistro Bl
and bl,1001010b;carichiamo il valore della lettere minuscola in binario

mov mess[8],bl

mov bl,mess[9]; carico il primo carattere sul reistro Bl
and bl,1001011b;carichiamo il valore della lettere minuscola in binario

mov mess[9],bl

mov bl,mess[10]; carico il primo carattere sul reistro Bl
and bl,1010001b;carichiamo il valore della lettere minuscola in binario

mov mess[10],bl



mov ah,09;mov si usa ah
lea dx,mess;usare dx per caricare la stringa dopo
int 21h

mess db 'AsDfGhJjjkq$'


ret




