node {
    stage('Get the code') {
        git credentialsId: 'b6b44b1f-71e5-49b9-89b6-fb29ae993b4e', poll: false, url: 'https://github.com/jemnem/myCatalogue.git'

    }
    stage('Deploy') {
        echo 'Deploying...'
    }
    stage('Test') {
        echo 'Testing...'
    }
}

