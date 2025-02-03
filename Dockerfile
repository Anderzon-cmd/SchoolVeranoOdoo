FROM odoo:18
USER root
# RUN apt-get update && apt-get install -y \
#     python3-dev \
#     python3.12-venv \
#     build-essential \
#     && rm -rf /var/lib/apt/lists/*

COPY ./modules /mnt/extra-addons
COPY ./requirements.txt /tmp/requirements.txt

# RUN chown -R odoo:odoo /mnt/extra-addons
# RUN python3 -m venv /opt/odoo-venv

# RUN /opt/odoo-venv/bin/pip install psycopg2
# RUN /opt/odoo-venv/bin/pip install --upgrade pip

# RUN apt install python3-numpy==2.1.3
# RUN python3 -m venv /opt/odoo/.venv
# ENV PATH="/opt/odoo/.venv/bin:$PATH"
RUN pip3 install --break-system-packages -r /tmp/requirements.txt

# USER odoo
# ENV PATH="/opt/odoo-venv/bin:$PATH"
USER odoo

EXPOSE 8069
CMD ["odoo", "-c", "/etc/odoo/odoo.conf"]


