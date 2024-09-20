<template>
  <div>
    <h2>Groups</h2>
    <AddToGroup :show="joinGroup" @exit="exitJoinToGroup"/>
    <GroupForm v-if="showForm" />
    <main>
      <div>
        <button class="action-button" @click="addToGroup">Join Group</button>
        <button v-if="!showForm" style="margin-left: 20px" @click="showForm = true" class="action-button">
          Add Group
        </button>
        <button v-if="showForm" style="margin-left: 20px" @click="showForm = false" class="action-button">
          Close
        </button>
        <h4>Teacher</h4>
        <ul>
          <li v-for="group in teacherGroups" :key="group.id">
            <div>
              <p>
                <strong>{{ group.title }}</strong> {{ group.group_id }} 
                <router-link class="button" :to="'/groups/' + group.group_id">View</router-link>
                <button
                style="margin-left: 20px" 
                  @click="confirmDeleteGroup(group.group_id)"
                  class="action-button"
                >
                  Delete
                </button>
              </p>
            </div>
            <DeleteGroup
              :show="selectedGroupId"
              :groupId="selectedGroupId"
              @delete="deleteGroup"
              @cancel="cancelDeleteGroup"
            />
          </li>
        </ul>
      </div>
      <div>
        <h4>Student</h4>
        <ul>
          <li v-for="group in studentGroups" :key="group.id">
            <div>
              <p>
                <strong>{{ group.title }}</strong> {{ group.group_id }}
                <router-link class="button" :to="'/groups/student/' + group.group_id">View</router-link>
              </p>
            </div>
          </li>
        </ul>
      </div>
    </main>
  </div>
</template>

<script>
import GroupForm from "./GroupForm.vue";
import DeleteGroup from "./modals/DeleteGroup.vue";
import AddToGroup from "./modals/AddToGroup.vue";

export default {
  components: {
    GroupForm,
    AddToGroup,
    DeleteGroup,
  },
  data() {
    return {
      showForm: false,
      selectedGroupId: null,
      joinGroup: false,
    };
  },
  computed: {
    teacherGroups() {
      return this.$store.state.teacherGroups;
    },
    studentGroups() {
      return this.$store.state.studentGroups;
    },
  },
  mounted() {
    this.$store.dispatch("fetchStudentGroups");
    this.$store.dispatch("fetchTeacherGroups");
  },
  methods: {
    addToGroup() {
      this.joinGroup = true;
    },
    confirmDeleteGroup(groupId) {
      this.selectedGroupId = groupId;
    },
    cancelDeleteGroup() {
      this.selectedGroupId = null;
    },
    deleteGroup() {
      this.$store.dispatch("deleteGroup", this.selectedGroupId);
      this.selectedGroupId = null;
    },
    exitJoinToGroup() {
      this.joinGroup = false;
    },
  },
};
</script>

<style scoped>
.action-button {
  background-color: #fff;
  border: none;
  color: teal;
  padding: 5px 10px;
  border-radius: 4px;
  cursor: pointer;
  border: 1px solid teal;
}

.button {
  background-color: #fff;
  border: none;
  color: teal;
  padding: 5px 10px;
  border-radius: 4px;
  cursor: pointer;
  border: 1px solid teal;
  text-decoration: none;
}

.button:hover {
  background-color: #f0f0f0;
}
.action-button:hover {
  background-color: #f0f0f0;
}
</style>
