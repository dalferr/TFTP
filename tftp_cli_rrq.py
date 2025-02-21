#!/usr/bin/env python3

import sys
import socket
import time

NULL  = b'\x00'
RRQ   = b'\x00\x01'
WRQ   = b'\x00\x02'
DATA  = b'\x00\x03'
ACK   = b'\x00\x04'
ERROR = b'\x00\x05'

PORT = 69
BLOCK_SIZE = 512

def get_file(s, serv_addr, filename):
    start = time.time()
    
    f = open(filename, 'wb')
    PETICION = RRQ + filename.encode() + NULL + 'octet'.encode() + NULL
    s.sendto(PETICION, serv_addr)
    expected_block = 1
    while True:
    
        RESPUESTA, dir_serv =  s.recvfrom(1024)
        OPCODE = RESPUESTA[0:2]
        
        if(OPCODE != DATA):
        
            exit(1)
            
        BLOQUE = RESPUESTA[2:4]
        BLOQUE2 = int.from_bytes(BLOQUE, 'big')
        if(BLOQUE2 == expected_block):
        
            DATOS = RESPUESTA[4:]
            f.write(DATOS)
            
            CONFIR = ACK + BLOQUE
            s.sendto(CONFIR, dir_serv)
        
            if(len(DATOS)<512):
            
                break
    
            expected_block += 1
    
    f.close()
    elapsed = time.time() - start
    bytes_received = (expected_block - 1) * BLOCK_SIZE + len(DATOS)
    print('{} bytes received in {:.2e} seconds ({:.2e} b/s).'.format(bytes_received, elapsed, bytes_received * 8 / elapsed))

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('Usage: {} server filename'.format(sys.argv[0]))
		exit(1)

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	serv_addr = (sys.argv[1], PORT)

	get_file(s, serv_addr, sys.argv[2])
