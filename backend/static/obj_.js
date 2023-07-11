new Vue({
    el: '#obj',
    data: {
    objects: []
    },
    mounted: function(){
        const vm = this;
        axios.get('/api/object/')
        .then(function(response){
        vm.objects = response.data
        })
    }
}

)