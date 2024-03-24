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
          <div>
            3334 results
          </div>
          <div v-for="result in filteredResults" :key="result.id" class="mb-3">
            <b-card
              :title="result.title"
              class="h-100">
              <p>{{ result.summary }}</p>
            </b-card>
          </div>
        </b-col>
      </b-row>
    </b-container>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue';
  
  const searchTerm = ref('');
  
  const searchResults = ref([
    // Your fake data or dynamic data
    { id: 1, title: 'Vue 3 and BootstrapVue', summary: 'Integrating Vue 3 with BootstrapVue for modern web applications.' },
    { id: 2, title: 'Component Design Patterns', summary: 'Exploring component design patterns in Vue 3 for scalable applications.' },
    // More results...
  ]);
  
  const filteredResults = computed(() => {
    return searchResults.value.filter(result => 
      result.title.toLowerCase().includes(searchTerm.value.toLowerCase()) || 
      result.summary.toLowerCase().includes(searchTerm.value.toLowerCase())
    );
  });
  </script>
  