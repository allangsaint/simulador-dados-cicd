pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'allangs/simulador-dados:v1'
        DOCKER_CRED_ID = 'dockerhub-id'
    }

    stages {
        stage('Limpieza del workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout del código') {
            steps {
                checkout scm
            }
        }

        stage('Análisis estático (Opcional)') {
            steps {
                echo 'Iniciando el escaneo de código estático...'
            }
        }

        stage('Construir imagen del contenedor') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Probar contenedor') {
            steps {
                script {
                    try {
                        echo 'Ejecutando pruebas sobre el contenedor...'
                        sh "docker run --name contenedor-prueba-cicd ${DOCKER_IMAGE}"
                    } finally {
                        echo 'Limpiando el contenedor de pruebas...'
                        sh "docker rm -f contenedor-prueba-cicd"
                    }
                }
            }
        }

        stage('Subir imagen a Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: "${DOCKER_CRED_ID}", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin"
                    sh "docker push ${DOCKER_IMAGE}"
                }
            }
        }
    }

    post {
        failure {
            echo '--------------------------------------'
            echo 'El pipeline ha fallado.'
            echo '--------------------------------------'
        }
    }
}