FROM ghcr.io/praekeltfoundation/python-base-nw:3.9-bullseye

RUN apt-get-install.sh nginx build-essential

COPY . /srv/wa_template_proxy
WORKDIR /srv/wa_template_proxy

RUN pip install -r requirements.txt --src /usr/local/src

RUN cp /srv/wa_template_proxy/nginx.conf /etc/nginx/
RUN chmod +x ./start.sh
CMD ["./start.sh"]
