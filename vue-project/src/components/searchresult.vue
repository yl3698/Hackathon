<template>
    <b-container class="mt-4">
      <b-row>
        <b-col cols="12" md="8" offset-md="2">
          <b-input-group class="mb-3">
            <b-form-input
              v-model="searchTerm"
              placeholder="Search..."
            ></b-form-input>
          </b-input-group>
          <!-- Dropdown for Year Filter -->
          <b-dropdown v-model="selectedYear" text="Year" variant="outline-secondary" class="m-3">
          <b-dropdown-item 
            v-for="year in years" 
            :key="year"
            :value="year"
          >
            {{ year }}
          </b-dropdown-item>
          </b-dropdown>
        
        <!-- Add additional dropdowns for other filters -->
          <b-dropdown v-model="selectedState" text="State" variant="outline-secondary" class="m-3">
            <b-dropdown-item 
              v-for="state in states" 
              :key="state"
              :value="state"
            >
            {{ state }}
            </b-dropdown-item>
            </b-dropdown>
          
          <b-dropdown text="Overturn" variant="outline-secondary" class="m-3">
            <b-dropdown-item>
              Yes
            </b-dropdown-item>
            <b-dropdown-item>
              No
            </b-dropdown-item>
          </b-dropdown>

          <b-dropdown text="Sort" variant="outline-secondary" class="m-3">
            <b-dropdown-item>
              Most Relevant
            </b-dropdown-item>
            <b-dropdown-item>
              Most Recent
            </b-dropdown-item>
            <b-dropdown-item>
              Most Cited
            </b-dropdown-item>
          </b-dropdown>

           
          <div class="bg-grey"> Selected states:
          <b-button>New York</b-button>
        </div>
          <p></p>
          <div class="bg-grey"> Year:
          <b-button >2024</b-button>
          <p></p>
          </div>

          <div v-for="result in filteredResults" :key="result.id" class="mb-3">  
            <b-card
              :subtitle="result.title"
              class="h-100"
              offset="2">
            </b-card>
          </div>
        </b-col>
      </b-row>
    </b-container>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue';
  

  const years = ref([...Array(new Date().getFullYear() - 2009 + 1).keys()].map(year => year + 2009).reverse());
  const selectedYear = ref(years.value[0]); // Default to the most recent year
  const states = ref(['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'New York', /* ... more states ... */ ]);
  const selectedState = ref(''); // Empty initial state or you can set a default one

  const searchTerm = ref('');
  
  const searchResults = ref([
    // Your fake data or dynamic data
    { id: 1, title: '1. Peterson Divorce Settlement Case', summary: 'Integrating Vue 3 with BootstrapVue for modern web applications.' },
    { id: 2, title: '2. Settlement Agreement and Divorce Decree', summary: 'Exploring component design patterns in Vue 3 for scalable applications.' },
    { id: 2, title: '3. something else about divorce', summary: 'Exploring component design patterns in Vue 3 for scalable applications.' },
    { id: 2, title: '4. something else about divorce2', summary: 'Exploring component design patterns in Vue 3 for scalable applications.' },
    { id: 2, title: '5. something else about divorce3', summary: 'Exploring component design patterns in Vue 3 for scalable applications.' },
    { id: 2, title: '6. something else about divorce4', summary: 'Exploring component design patterns in Vue 3 for scalable applications.' },
    { id: 2, title: '7. something else about divorce5', summary: 'Exploring component design patterns in Vue 3 for scalable applications.' },
    { id: 2, title: '8. something else about divorce6', summary: 'Exploring component design patterns in Vue 3 for scalable applications.' },
    { id: 2, title: '9. something else about divorce7', summary: 'Exploring component design patterns in Vue 3 for scalable applications.' },
    // More results...
  ]);
  
  const filteredResults = computed(() => {
    return searchResults.value.filter(result => 
      result.title.toLowerCase().includes(searchTerm.value.toLowerCase()) || 
      result.summary.toLowerCase().includes(searchTerm.value.toLowerCase())
    );
  });
  </script>

  <style>
.bg-grey {
  color: grey;
}</style>
  