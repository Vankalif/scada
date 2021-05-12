const Counter = {
    data() {
      return {
        wells: {},
      }
    },

    created() {
        fetch('http://localhost:8000/get_wells').then(wells => {
            return wells.json();
        }).then(data => {
            this.wells = data;
        });
    },

    methods: {

    }
  }
  
  Vue.createApp(Counter).mount('#app')
  