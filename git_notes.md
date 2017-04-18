# Git Notes
## Git General
```
git init
git status
git add .
git commit -m "Initial Upload"
git config --global user.name "yourname"
git config --global user.email "youremail@gmail.com"
git config --global credential.helper cache
git remote add REPO git@github.com:tylerhardy/REPO.git
git push -u REPO master
<!--git push --set-upstream REPO master-->
```
## SSH MAC
### Generating SSH MAC
```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
eval "$(ssh-agent -s)"
ssh-add -K ~/.ssh/id_rsa
```
- For macOS Sierra 10.12 or later, modify your `~/.ssh/config` file:
```
Host *
 AddKeysToAgent yes
 UseKeychain yes
 IdentityFile ~/.ssh/id_rsa
```
### Adding SSH key to GitHub MAC
```
pbcopy < ~/.ssh/id_rsa.pub
```
## SSH PC
### Generating SSH PC
```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa
```
### Adding SSH key to GitHub PC
```
clip < ~/.ssh/id_rsa.pub
```
## Testing SSH
```
ssh -T git@github.com
```
