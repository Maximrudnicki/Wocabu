<template>
  <div>
    <h2>Sets</h2>
    <SetForm v-if="showForm" />
    <div>
        <button v-if="!showForm" @click="showForm = true" class="action-button">
          Add Set
        </button>
        <button v-if="showForm" @click="showForm = false" class="action-button">
          Close
        </button>
      <ul>
        <li v-for="set in sets" :key="set._id">
          <div>
            <p>
              <strong>{{ set.name }}</strong> {{ set._id }}
              <router-link class="button" :to="'/sets/' + set._id"
                >View</router-link
              >
              <button
                style="margin-left: 20px"
                @click="confirmDeleteSet(set._id)"
                class="action-button"
              >
                Delete
              </button>
            </p>
          </div>
          <DeleteSet
              :show="selectedSetId"
              :setId="selectedSetId"
              @delete="deleteSet"
              @cancel="cancelDeleteSet"
            />
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import SetForm from "./SetForm.vue";
import DeleteSet from "./modals/DeleteSet.vue";

export default {
  components: {
    SetForm,
    DeleteSet,
  },
  data() {
    return {
      showForm: false,
      selectedSetId: null,
    };
  },
  computed: {
    sets() {
      return this.$store.state.sets;
    },
  },
  mounted() {
    this.$store.dispatch("fetchSets");
  },
  methods: {
    confirmDeleteSet(setId) {
      this.selectedSetId = setId;
    },
    cancelDeleteSet() {
      this.selectedSetId = null;
    },
    deleteSet() {
      this.$store.dispatch("deleteSet", this.selectedSetId);
      this.selectedSetId = null;
    },
  },
};
</script>

<style scoped></style>
