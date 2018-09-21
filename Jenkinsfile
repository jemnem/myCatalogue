node ('api-test') {
    stage('Get the code from githut') {
       git credentialsId: 'b6b44b1f-71e5-49b9-89b6-fb29ae993b4e', url: 'https://github.com/jemnem/myCatalogue.git'
    }
    stage('Deploy') {
        echo 'start deploying...'
        sh 'docker-compose stop'
        sh 'docker-compose build'
        sh 'docker-compose up -d'
    }
    stage('Test') {
        echo ' start testing...'
    }
}

