window.addEventListener('load', async function(event){
    let response = await this.fetch('http://localhost:8000/api/categories/')
    let resDataCategories = await response.json()
    let recipeCategory = this.document.getElementById('recipe-category')
    for (category of resDataCategories){
        recipeCategory.innerHTML += `
             <option value="${category.id}">${category.title}</option>
        `
    }
    let responseTags = await this.fetch('http://localhost:8000/api/tags/')
    let resDataTags = await responseTags.json()
    let recipeTags = this.document.getElementById('recipe-tags')
    for (tag of resDataTags){
        recipeTags.innerHTML += `
             <option value="${tag.id}">${tag.title}</option>
        `
    }

})

let recipeCreationForm = document.querySelector('#recipe-creation-form')
let token = localStorage.getItem('token')
recipeCreationForm.addEventListener('submit', async function(event){
    event.preventDefault()
    let formData = new FormData(recipeCreationForm)
    let responseForm  = await fetch('http://localhost:8000/api/recipes/', {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${token}`
        },
        body: formData
    })
    console.log(await responseForm.json())
})