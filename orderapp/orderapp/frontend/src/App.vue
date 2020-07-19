/* eslint-disable */
<template>
  <div id="app">
 <div>
    <div class = "search">
      <b-input-group prepend="Search" class="mb-2 mr-sm-2 mb-sm-0">
        <b-form-input v-model="value" type="text" debounce="500"> </b-form-input>
      </b-input-group>
    </div>
    <label for="example-datepicker">Choose a date range</label>
    <b-form inline>
      <b-form-datepicker id="example-datepicker" v-model="startdate" class="date mb-2"></b-form-datepicker>
      <b-form-datepicker id="example-datepicker" v-model="finaldate" class="date mb-2"></b-form-datepicker>
      <p><b>Total Amount</b>     ${{ total_amount }}</p>
    </b-form>
    </div>
    <b-container>
     <!-- Content here -->
         <b-row>
        <b-col col md="12">
            <b-table :items="items"
            :current-page="currentPage"
            :per-page="perPage"
            :filter="value"
            ></b-table>
        </b-col>
    </b-row>
    <b-row>
        <b-col col md="12">
            <!-- <p>Total 2</p> -->
            <b-pagination
          v-model="currentPage"
          :total-rows="totalRows"
          :per-page="perPage"
          align="fill"
          size="sm"
          class="my-0"
        ></b-pagination>
        </b-col>
    </b-row>
    </b-container>

    
  </div>
</template>
<script> 
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Vue from 'vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import moment from "moment"
// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
export default {
    name: 'App',
    data() {
      return {
        value: '',
        startdate: '',
        finaldate: '',
        items: [],
        orders:[{"id":1,"created_at":"1\/2\/2020","order_name":"PO #001-I","customer_name":"Ivan Ivanovich","Company Name":"Roga & Kopyta","total_amount":918.122,"Product Names":" Corrugated Box,Hand sanitizer","Delivered Amount":6.727},{"id":2,"created_at":"1\/15\/2020","order_name":"PO #002-I","customer_name":"Ivan Ivanovich","Company Name":"Roga & Kopyta","total_amount":254.54,"Product Names":" Corrugated Box,Hand sanitizer","Delivered Amount":254.54},{"id":3,"created_at":"1\/5\/2020","order_name":"PO #003-I","customer_name":"Ivan Ivanovich","Company Name":"Roga & Kopyta","total_amount":7485.1288,"Product Names":" Corrugated Box,Hand sanitiZER","Delivered Amount":1476.414},{"id":4,"created_at":"2\/2\/2020","order_name":"PO #004-I","customer_name":"Ivan Ivanovich","Company Name":"Roga & Kopyta","total_amount":263.35,"Product Names":" Corrugated Box,Hand sanitizer","Delivered Amount":0.0},{"id":5,"created_at":"1\/3\/2020","order_name":"PO #005-I","customer_name":"Ivan Ivanovich","Company Name":"Roga & Kopyta","total_amount":1699.208,"Product Names":" Corrugated Box,Hand sanitizer","Delivered Amount":0.0},{"id":6,"created_at":"1\/2\/2020","order_name":"PO #001-P","customer_name":"Petr Petrovich","Company Name":"Pupkin & Co","total_amount":298.181,"Product Names":" Corrugated Box,Hand sanitizer","Delivered Amount":298.181},{"id":7,"created_at":"1\/15\/2020","order_name":"PO #002-P","customer_name":"Petr Petrovich","Company Name":"Pupkin & Co","total_amount":3600.24,"Product Names":" Corrugated Box,Hand sanitizer","Delivered Amount":3399.12},{"id":8,"created_at":"1\/5\/2020","order_name":"PO #003-P","customer_name":"Petr Petrovich","Company Name":"Pupkin & Co","total_amount":6935.9183,"Product Names":" Corrugated Box,Hand sanitizer","Delivered Amount":6935.9183},{"id":9,"created_at":"2\/2\/2020","order_name":"PO #004-P","customer_name":"Petr Petrovich","Company Name":"Pupkin & Co","total_amount":910.736,"Product Names":" Corrugated Box,Hand sanitizer","Delivered Amount":668.528},{"id":10,"created_at":"1\/3\/2020","order_name":"PO #005-P","customer_name":"Petr Petrovich","Company Name":"Pupkin & Co","total_amount":5570.0,"Product Names":" Corrugated Box,Hand sanitizer","Delivered Amount":3480.0}],
        totalRows: null,
        currentPage: 1,
        perPage: 5,
        total_amount: 0,
      }

    },
     mounted() {
      // Set the initial number of items
      this.totalRows = this.orders.length
      for(var temp of this.orders){
        this.total_amount += temp.total_amount;
        this.total_amount = Math.round(this.total_amount);
        temp.created_at = new Intl.DateTimeFormat('en-US', { year: 'numeric', month: 'short', day: '2-digit' }).format(new Date(Date.parse(temp.created_at)));

        console.log(temp.created_at);
        if (this.startdate != '' && this.finaldate != ''){
            this.startdate = new Intl.DateTimeFormat('en-US', { year: 'numeric', month: 'short', day: '2-digit' }).format(new Date(Date.parse(this.startdate)));
            this.finaldate = new Intl.DateTimeFormat('en-US', { year: 'numeric', month: 'short', day: '2-digit' }).format(new Date(Date.parse(this.finaldate)));
            console.log(this.startdate);
            console.log(this.finaldate);
            if ((this.startdate.localeCompare(temp.created_at) === 0 || this.startdate.localeCompare(temp.created_at) === 1) && (this.finaldate.localeCompare(temp.created_at) === 0 || this.finaldate.localeCompare(temp.created_at) === -1)){
              this.items.push(temp);
            }
          }
        else {
          this.items.push(temp);
        }
        }
      
    },


    methods: {
        onFiltered(filteredItems) {
        // Trigger pagination to update the number of buttons/pages due to filtering
        this.totalRows = filteredItems.length
        this.currentPage = 1
      }
    }
    
 
  
}

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: 50px 75px;
}
.date {
  margin-right: 100px;
}
.search {
  padding-right: 75px;
  padding-bottom: 50px;
}

</style>
