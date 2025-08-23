# Étape 1 : Build de l'app React
FROM node:18 AS build

WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

# Étape 2 : Serveur NGINX pour servir les fichiers statiques
FROM nginx:alpine

COPY --from=build /app/dist /usr/share/nginx/html

# Remplace la config par défaut de NGINX
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
