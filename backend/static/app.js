new Vue
({
            el:'#app_tab',
            data: () =>(
            {
                items: [

                ],
                fields: [
                ],
                totalRows: 1,
                currentPage: 1,
                perPage: 10,
                pageOptions: [10, 15, { value: 100000, text: "Показать все" }],
                sortBy: '',
                sortDesc: false,
                sortDirection: 'asc',
                filter: null,
                filterOn: [],
                infoModal: {
                  id: 'info-modal',
                  title: '',
                  content: ''
                            }

            }
            ),
            computed: {
              sortOptions() {
                // Create an options list from our fields
                return this.fields
                  .filter(f => f.sortable)
                  .map(f => {
                    return { text: f.label, value: f.key }
                  })
              }
            },
            mounted() {
              // Set the initial number of items
              this.getApiFields_list();
              this.getApiOtkaz_list();
              this.totalRows = this.items.length

            },
            methods: {
              info(item, index, button) {
                this.infoModal.title = `Row index: ${index}`
                this.infoModal.content = JSON.stringify(item, null, 2)
                this.$root.$emit('bv::show::modal', this.infoModal.id, button)
              },
              resetInfoModal() {
                this.infoModal.title = ''
                this.infoModal.content = ''
              },
              onFiltered(filteredItems) {
                // Trigger pagination to update the number of buttons/pages due to filtering
                this.totalRows = filteredItems.length
                this.currentPage = 1
              },
              getApiFields_list: function()
                {
                    //const vm = this;
                    axios.get('/api_get_fields_list/')
                    .then(function(response){
                    this.fields = response.data
                    }.bind(this));
                },
              getApiOtkaz_list: function()
                {
                    //const vm = this;
                    axios.get('/api_get_otkaz_list/')
                    .then(function(response){
                    this.items = response.data
                    }.bind(this));
                },
            }
})
new Vue({
  el:'#add_prilozh_app',
  data:{
    prilozh:false,
    prilozh_count:0,
  },
  // methods{
  //   add_prilozh(){
  //     this.prilozh_count = this.prilozh_count+ 1;
  //   },
  //   delete_prilozh(){
  //     this.prilozh_count = this.prilozh_count+ 1;
  //   }
  // }

})

/*new Vue({
    el:'#otkaz_app',
    data:{
    otkaz_list:[]
    },
    methods:
    {
    getApiOtkaz_list: function()
        {
            //const vm = this;
            axios.get('/api_get_otkaz_list/')
            .then(function(response){
            this.otkaz_list = response.data
            }.bind(this));
        },
    },
    mounted:function()
    {
       this.getApiOtkaz_list();
    }
})*/

/*new Vue({
  el: '#ap_p_table',
  data: () => ({
    fields: [

    ],
    filter: {
      continent: null,
      population: null,
    },
    continents: [ { text: '-', value: null }, 'Европа', 'Азия', 'Северная Америка' ],
    populations: [
      { text: '-', value: null },
      { text: '[ 0, 50 )', value: [ 0, 50 ] },
      { text: '[ 50, 100 )', value: [ 50, 100 ] },
      { text: '[ 100, +∞ )', value: [ 100, Infinity ] },
    ],
    otkaz: [
      /*{ act_number: 'Япония', model: 126.2, maker: 'Азия' },
      { act_number: 'Франция', model: 67, maker: 'Европа' },
      { act_number: 'Италия', model: 60.8, maker: 'Европа' },
      { act_number: 'США', model: 327.6, maker: 'Северная Америка' },
      { act_number: 'Малайзия', model: 31, maker: 'Азия' },
      { act_number: 'Вьетнам', model: 92.5, maker: 'Азия' },
      { act_number: 'Канада', model: 37.3, maker: 'Северная Америка' },
      { act_number: 'Мексика', model: 133.1, maker: 'Северная Америка' },
      { act_number: 'Норвегия', model: 5.3, maker: 'Европа' },
      { act_number: 'Китай', model: 1395.4, maker: 'Азия' },
    ],
  }),
  methods: {
    filterFunction(row, val) {
      const { continent: c, population: p } = val;
      return [
        !c || c === row.continent,
        !p || p[0] <= row.population && p[1] > row.population,
      ].every(Boolean);
    },
    getApiFields_list: function()
        {
            //const vm = this;
            axios.get('/api_get_fields_list/')
            .then(function(response){
            this.fields = response.data
            }.bind(this));
        },
    getApiOtkaz_list: function()
    {
        //const vm = this;
        axios.get('/api_get_otkaz_list/')
        .then(function(response){
        this.otkaz = response.data
        }.bind(this));
    },
  },
  mounted:function()
    {
       this.getApiFields_list();
       this.getApiOtkaz_list();
    }
})*/
