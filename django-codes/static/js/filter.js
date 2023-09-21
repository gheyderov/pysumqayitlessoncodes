const FilterLogic = {
    url: `${location.origin}/api/recipes/`,

    filterRecipes(category){
        let url = this.url
        if (category) {
            url += `?category=${category}`
        }
        fetch(url).then(response => response.json()).then(data =>{
            document.getElementById('recipe-list').innerHTML = ''
            for (let i in data){
                document.getElementById('recipe-list').innerHTML += `
                <div class="col-md-6 col-lg-12">
                <div class="blog-entry d-lg-flex">
                    <div class="half">
                        <a href="/recipe/${data[i].slug}/" class="img d-flex align-items-end"
                           style="background-image: url(${data[i].image});">
                            <div class="overlay"></div>
                        </a>
                    </div>
                    <div class="text px-md-4 px-lg-5 half pt-3">
                        <p class="meta d-flex"><span class="pr-3">${data[i].category.title}</span><span class="ml-auto pl-3"></span>
                        </p>
                        <h3><a href="/recipe/${data[i].slug}/">${data[i].title}</a></h3>
                        <p>${data[i].description}
                        </p>
                        <p class="mb-0">
                            <a href="" class="btn btn-primary">Like</a>
                            <a href="/recipe/${data[i].slug}/" class="btn btn-primary">Read More <span
                                class="icon-arrow_forward ml-4"></span></a>
                            </p>
                    </div>
                </div>
            </div>
                `
            }
        })
    }
}



let recipeCategory = document.getElementsByClassName('category-filter')
for (let i = 0; recipeCategory.length; i++){
    recipeCategory[i].addEventListener('click', function(event){
        event.preventDefault()
        const category = this.getAttribute('data')
        console.log(category)
        FilterLogic.filterRecipes(category)
    })
}