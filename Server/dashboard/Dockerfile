FROM php:8.3.14-apache-bookworm

RUN apt-get -y update --fix-missing && \
    apt-get upgrade -y && \
    apt-get --no-install-recommends install -y apt-utils && \
    rm -rf /var/lib/apt/lists/*
	
RUN rm /etc/apt/preferences.d/no-debian-php

RUN apt-get update && apt-get install -y \
		libfreetype6-dev \
		libjpeg62-turbo-dev \
		libpng-dev \
		build-essential \
		libcurl4-openssl-dev \
		libssl-dev \
		libpq-dev \
		git \
		libonig-dev \
		# libbz2-dev \
		zlib1g-dev \
		libxml2-dev \
		zip \
		unzip \
		libzip-dev \
	&& docker-php-ext-configure gd --with-freetype --with-jpeg \
	&& docker-php-ext-install -j$(nproc) gd

# RUN /usr/local/bin/phpize

######################################[INSTALL EXTENSI PHP]####################################
# RUN docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql 
# RUN	docker-php-ext-install pdo pdo_pgsql pgsql
RUN	docker-php-ext-install mysqli
RUN	docker-php-ext-install curl 
RUN	docker-php-ext-install mbstring 
RUN	docker-php-ext-install bcmath
RUN	docker-php-ext-install xml
RUN	docker-php-ext-install zip

#------------------------------------[AKTIFKAN UNTUK DEVELOPMEN]-------------------------------
RUN	pecl install xdebug && docker-php-ext-enable xdebug

# ENABLE REWRITE & RESTART APACHE
RUN a2enmod rewrite \ 
	&& service apache2 restart

EXPOSE 80/tcp
