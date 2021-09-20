#Instructions

Step1: Containerise the application 
Step2 : Install minikube for kubernetes functionality
Step3 : Deploy containerised application onto to kubernetes

#Step1: Containerise the application 
Using docker:
1. Create DockerFile. 
2. Build image.  
cmd: docker build -t fastapi_okrapp_kubernetes .
3. Verify image created.  
cmd: docker images 

#Step2 : Install minikube for kubernetes functionality
Install minikube following link : 
1. Verify minikube installation.  
cmd: minikube version
2. Start minikube.  
cmd: minikube start
3. Launch minikube dashboard.  
cmd: minikube dashboard 

#Step3 : Deploy containerised application onto to kubernetes
1. Create a YAML file for deployment with appropriate inputs
for service, deployment sections. 
2. Using deployment.yaml file to create deployment in kubernetes.
cmd: kubectl apply -f deployment.yaml
3. Verify pods creation.  
cmd: kubectl get pods
4. Verify the pods, deployment & services created on minikube
dashboard in respective tabs and make sure no errors.
5. To access the application on local computer, port-forwarding
is needed from containerport to port on local computer.  
cmd: kubectl port-forward fastapi-test-okr-app-57f67cdd7f-fn5ln 8000:8000 
here: fastapi-test-okr-app-57f67cdd7f-fn5ln -> pod created in previous step.
