pipeline {
    agent any

    environment {
        DOCKER_IMAGE_BASE = "app-python-base"
        DOCKER_IMAGE_APP  = "app-python-final"
        CONTAINER_NAME    = "mi-aplicacion-python"
    }

    stages {
        stage('1. Recuperar Código') {
            steps {
                echo 'Descargando código desde GitHub...'
                checkout scm
            }
        }

        stage('2. Construir Imagen Base') {
            steps {
                echo 'Construyendo la imagen Docker Base...'
                sh "docker build -t ${DOCKER_IMAGE_BASE} -f Dockerfile.base ."
            }
        }

        stage('3. Construir Imagen Aplicativa') {
            steps {
                echo 'Construyendo la imagen Docker Final...'
                sh "docker build -t ${DOCKER_IMAGE_APP} -f Dockerfile ."
            }
        }

        stage('4. Desplegar Aplicación') {
            steps {
                echo 'Limpiando contenedores anteriores...'
                sh "docker stop ${CONTAINER_NAME} || true"
                sh "docker rm ${CONTAINER_NAME} || true"
                
                echo 'Levantando el nuevo contenedor de la aplicación...'
                sh "docker run -d --name ${CONTAINER_NAME} ${DOCKER_IMAGE_APP}"
            }
        }
    }
}
