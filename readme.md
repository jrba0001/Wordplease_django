# Práctica de Python, Django y REST
### José R. Bonilla Alarcón
Se desea crear una plataforma de blogging llamada Wordplease en la cual los usuarios puedan registrarse para crear su blog personal.

## Sitio WEB
* En la página principal, deberán aparecer los últimos posts publicados por los usuarios.
`Se accede a la home, listado fecha publicación más reciente, se listan 5.`
* En la URL /blogs/, se deberá mostrar un listado de los blogs de los usuarios que hay en laplataforma.
`http://127.0.0.1:8000/blog`
* El blog personal de cada usuario, se cargará en la URL /blogs/<nombre_de_usuario>/ donde aparecerán todos los posts del usuario ordenados de más actual a más antiguo (los últimos posts primero).
`http://127.0.0.1:8000/blog/jrbonilla/. También se puede acceder desde la opción de menú, en listar blog's y dentro del listado, tendremos opción de listar los post de cada blog`
* En la URL /blog/<nombre_de_usuario/<post_id> se deberá poder ver el detalle de un post.
`http://127.0.0.1:8000/detalle/3 Se puede acceder al detalle de un post, desde el listado home, de post recientes, en detalles, como en listado de blogs, opcion listar post y dentro detalle`
* Un post estará compuesto de: título, texto a modo de introducción, cuerpo del post, URL deimagen o vídeo destacado (opcional), fecha y hora de publicación (para poder publicar un posten el futuro), categorías en las que se publican (un post puede publicarse en una o variascategorías). Las categorías deben poder ser gestionadas desde el administrador.
`Realizado`
* Tanto en la página principal como en el blog personal de cada usuario, se deberán listar los posts con el mismo diseño/layout. Para cada post deberá aparecer el título, la imagen destacada (si tiene) y el resumen.
`Realizado`
* En la URL /login el usuario podrá hacer login en la plataforma.
`Realizado`* En la URL /logout el usuario podrá hacer logout de la plataforma.
`Realizado`* En la URL /signup el usuario podrá registrarse en la plataforma indicando su nombre, apellidos, nombre de usuario, e-mail y contraseña.
`Realizado`
* En la URL /new-post deberá mostrarse un formulario para crear un nuevo post. Para acceder a esta URL se deberá estar autenticado. En formulario para crear el post deberá identificar al usuario autenticado para publicar el POST en el blog del usuario.
`Realizado`

## API REST

#### API de blogs
`**Realizado en endpoint "http://127.0.0.1:8000/api/v1/api_blog/"**`
• Un endpoint que no requiera autenticación y devuelva el listado de blogs que hay en la plataforma con la URL de cada uno. Este endpoint debe permitir buscar blogs por el nombre del usuario y ordenarlos por nombre.
`Desde la dirección http://127.0.0.1:8000/api/v1/, se accederá al api root. se habilita el router   "api_blog": "http://127.0.0.1:8000/api/v1/api_blog/"
}`

#### API de usuarios
`** Realizado en endpoint http://127.0.0.1:8000/api/v1/users/**`
* Endpoint que permita a cualquier usuario registrarse indicando su nombre, apellidos, nombre de usuario, e-mail y contraseña.
* Endpoint que permita ver el detalle de un usuario. Sólo podrán ver el endpoint de detalle de un usuario el propio usuario o un administrador. 
* Endpoint que permita actualizar los datos de un usuario. Sólo podrán usar el endpoint de un usuario el propio usuario o un administrador.
* Endpoint que permita eliminar un usuario (para darse de baja). Sólo podrán usar el endpoint de un usuario el propio usuario o un administrador. 

#### API de post
`**Realizado en endopoint http://127.0.0.1:8000/api/v1/posts/
**`

* Un endpoint para poder leer los artículos de un blog de manera que, si el usuario no está autenticado, mostrará sólo los artículos publicados. Si el usuario está autenticado y es el propietario del blog o un administrador, podrá ver todos los artículos (publicados o no). En este endpoint se deberá mostrar únicamente el título del post, la imagen, el resumen y la fecha de publicación. Este endpoint debe permitir buscar posts por título o contenido y ordenarlos por título o fecha de publicación. Por defecto los posts deberán venir ordenados por fecha de publicación descendente. ``* Un endpoint para crear posts en el cual el usuario deberá estar autenticado. En este endpoint el post quedará publicado automáticamente en el blog del usuario autenticado.* Un endpoint de detalle de un post, en el cual se mostrará toda la información del POST. Si el post no es público, sólo podrá acceder al mismo el dueño del post o un administrador.* Un endpoint de actualización de un post. Sólo podrá acceder al mismo el dueño del post o un administrador.* Un endpoint de borrado de un post. Sólo podrá acceder al mismo el dueño del post o un administrador.