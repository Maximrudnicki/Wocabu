<template>
    <div>
      <p></p>
      <div v-if="group">
        <p><router-link class="button" to="/groups/">Back</router-link>
          <strong style="font-size: 24px; margin-left: 20px;">{{ group.title }}</strong> <span style="font-size: 24px;">{{ group.group_id }}</span>
        </p>
        <p>
          <strong style="font-size: 24px;">Teacher: {{teacher.username}}, {{teacher.email}}</strong>
        </p>
        <ul v-for="student in group.students">
          <li v-if="student.student_id === group.user_id">
            <div >
              {{ student.username }}
              <router-link
                class="button"
                :to="'/groups/student/' + group.group_id + '/' + student.student_id"
                >View Details</router-link
              >
              <StudentDetails
                :show="showStudentDetails"
                :student="studentDetails"
                @cancel="cancelStudentDetails"
              />
            </div> <br>
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import StudentDetails from "./modals/StudentDetails.vue";
  
  export default {
    components: {
      StudentDetails,
    },
    data() {
      return {
        showStudentDetails: null,
        studentDetails: null,
      };
    },
    mounted() {
      const formData = {
        group_id: this.$route.params.id,
      };
      this.$store.dispatch("fetchGroup", formData);
      this.$store.dispatch("findTeacher", formData);
    },
    computed: {
      group() {
        return this.$store.state.group;
      },
      teacher() {
        return this.$store.state.teacher;
      },
    },
    methods: {
      showDetails(studentId) {
        console.log(studentId);
        this.showStudentDetails = studentId;
      },
      cancelStudentDetails() {
        this.showStudentDetails = null;
      },
      findStudent(studentId, groupId) {
        const formData = {
          student_id: studentId,
          group_id: groupId,
        };
        const studentPromise = this.$store.dispatch("findStudent", formData);
        studentPromise.then((studentDetails) => {
          this.studentDetails = studentDetails;
        });
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
  