node ('api-test') {
    stage('Get the code') {
       git credentialsId: 'b6b44b1f-71e5-49b9-89b6-fb29ae993b4e', url: 'https://github.com/jemnem/myCatalogue.git'
       sh 'echo $PWD'
    }
    stage('Deploy') {
        echo 'start deploying...'
    }
    stage('Test') {
        echo ' start testing...'
    }
}

