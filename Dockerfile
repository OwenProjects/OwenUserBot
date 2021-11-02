# FROM kısmını Değiştirmeyiniz Owenye DockerFile Kullanın

FROM erdembey/epicuserbot:latest
RUN git clone https://github.com/erdewbey/OwenUserBot /root/OwenUserBot
WORKDIR /root/OwenUserBot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]  
