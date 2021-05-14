class Well {

  constructor(well_id){

    this.temperature = new function(){

      setInterval( async () => {
        const resp = await fetch(`http://localhost:8000/get_last_in/temperature/${well_id}`);
        const val = await resp.json();
        this.value = val[0][1];
      }, 5000);

    };

    this.level = new function(){

      setInterval( async () => {
        const resp = await fetch(`http://localhost:8000/get_last_in/level/${well_id}`);
        const val = await resp.json();
        this.value = val[0][1];
      }, 5000);

    };
    
    this.pressure = new function(){

      setInterval( async () => {
        const resp = await fetch(`http://localhost:8000/get_last_in/pressure/${well_id}`);
        const val = await resp.json();
        this.value = val[0][1];
      }, 5000);

    };

  };

}


const LiveApp = {
    data() {
      return {
        wells: {},
      }
    },

    created() {
        fetch('http://localhost:8000/get_wells').then(resp => {
            return resp.json();
        }).then(data => {
            for (var key in data){
              data[key].telemetry = new Well(data[key].well_id)
            }
            this.wells = data;
            console.log(data);
        });
    },

    methods: {

    }
  }
  
  Vue.createApp(LiveApp).mount('#app')
  