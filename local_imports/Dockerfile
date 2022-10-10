FROM python:3.7-slim
LABEL org.opencontainers.image.source.=https://github.com/poshkaran04/data_pipelines

# apt-get and system utilities
RUN apt-get update && apt-get install -y \
curl apt-utils apt-transport-https debconf-utils gcc build-essential\
    && rm -rf /var/lib/apt/lists/*

# adding custom MS repository
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

# install SQL Server drivers
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev

# install necessary locales
RUN pip3 install --upgrade pip

COPY requirements requirements
RUN pip3 install -r requirements

COPY /src /src

WORKDIR /src

ENTRYPOINT ["python","etl_csv_mssql.py"]