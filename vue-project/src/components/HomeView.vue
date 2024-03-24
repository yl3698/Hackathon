<script setup lang="ts">
import { ref } from 'vue';
const groupedSelected = ref("defs")

const tagCategories = [
  "legal education and writing",
  "THE LEGAL PROCESS",
  "criminal law",
  "criminal procedure",
  "civil procedure",
  "legal theory",
  "courts and procedure",
  "criminal law and procedure",
  "legal education and practice",
  "wex definitions"
]
</script>

<template>
  <img src="../assets/header.png" alt="Header Image" class="full-width-image">
  <div class="main-component">
    <div class="header-text">
      <h1>Welcome to Wex, Lll’s community-built</h1>
      <p style="font-size: large;">Freely available legal dictionary and legal encyclopedia</p>
    </div>
    <div>
      <BContainer class="search-field">
        <BRow class="field-row">
          <BCol cols="4">
            <BFormRadioGroup id="radio-group-2" v-model="groupedSelected" name="radio-sub-component">
              <BFormRadio value="defs">Definitions</BFormRadio>
              <BFormRadio value="cases">Court Cases</BFormRadio>
            </BFormRadioGroup>
          </BCol>
          <BCol cols="8">
            <BNavbar class="search-bar">
              <BNavForm class="search-bar">
                <BFormInput class="me-sm-2 search-bar" placeholder="Search for Definitions or Court Cases" />
                <BButton variant="outline-success" class="my-2 my-sm-0" type="submit"><svg
                    xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search"
                    viewBox="0 0 16 16">
                    <path
                      d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0" />
                  </svg></BButton>
              </BNavForm>
            </BNavbar>
          </BCol>
        </BRow>
      </BContainer>
      <div class="small-text" v-if="groupedSelected === 'defs'">
        <p class="small-text">
          Wex Definitions Team
        </p>
      </div>

    </div>

    <div class="wordcloud" v-if="groupedSelected === 'defs'">
      <span v-for="tag of tagCategories" class="m-2 badge rounded-pill text-bg-secondary">{{ tag }}</span>
    </div>

    <div v-if="groupedSelected !== 'defs'" class="view-all">
      <BButton href="#">View All</BButton>
    </div>
  </div>

</template>

<style scoped>
.full-width-image {
  width: 100%;
  height: 150px;
}

.view-all {
  justify-content: center;
  display: flex;

}

.small-text {
  display: flex;
  justify-content: center;
  color: #B31A1B;
}

.wordcloud {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  max-width: 800px;
  margin: auto;
  margin-top: 0px;
  margin-bottom: 0px;
}

.main-component {
  height: 500px;
  justify-content: center;
  display: flex;
  flex-direction: column;
}

.rounded-pill {
  padding-top: 10px;
  padding-bottom: 10px;
  padding-left: 20px;
  padding-right: 20px;
}

.field-row {
  align-items: center;
}

.form-check-inline {
  display: inline-block;
  margin-right: 0.5rem;
}

.search-field {
  width: 800px;
  justify-content: center;
  display: flex;
  align-items: center;
}

.header-text {
  width: 100%;
  justify-content: center;
  align-items: center;
  display: flex;
  flex-direction: column;
  color: black;
}

.search-bar {
  width: 500px;
}

h1 {
  font-weight: 700 !important;
}
</style>
