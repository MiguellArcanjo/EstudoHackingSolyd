# Esse bash foi criado nos estudos de ciber segurança com o intuito de praticar os conhecimentos aprendidos na aula de shellScript e criptografia.


#!/bin/bash

echo "Digite a senha que você quer criptografar: "
read senha

echo "$senha:$(echo -n "$senha" | md5sum)" >> senhas_criptografadas.txt

echo "Pressione A para ver todas as senhas criptografadas ou O para ver apenas a senha atual: "
read opcao

if [ "$opcao" == "A" ]
then 
echo "Senhas criptografadas: "
cat senhas_criptografadas.txt

elif [ "$opcao" == "O" ]
then
echo "Senha criptografada: "
echo -n "$senha" | md5sum

fi