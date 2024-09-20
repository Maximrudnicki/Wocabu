<template>
  <div>
    <p></p>
    <router-link class="button" to="/groups/">Back</router-link>
    <div v-if="group">
      <p>
        <strong style="font-size: 24px;">{{ group.title }}</strong> <span style="font-size: 20px;">{{ group.group_id }}</span>
      
      <button style="margin-left: 10px;" v-if="!showTable" @click="showTable = true" class="action-button">
        Statistics
      </button>
      <button style="margin-left: 10px;" v-if="showTable" @click="showTable = false" class="action-button">
        Close
      </button>
    </p>
      <table v-if="showTable">
        <thead>
          <tr>
            <th>ID</th>
            <th>Email</th>
            <th>Username</th>
            <th>Total Trainings</th>
            <th>Completed Trainings</th>
            <th>Total Words</th>
            <th>Learned words</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="student in group.students" :key="student.student_id">
            <td>{{ student.student_id }}</td>
            <td>{{ student.email }}</td>
            <td>{{ student.username }}</td>
            <td>{{ student.words.length * 4 }}</td>
            <td :class="{
            'is-true': completedTrainings(student.words) === student.words.length * 4 && completedTrainings(student.words) !== 0,
            'is-false': completedTrainings(student.words) !== student.words.length * 4
          }">{{ completedTrainings(student.words) }}</td>
            <td>{{ student.words.length }}</td>
            <td :class="{
            'is-true': learnedWords(student.words) === student.words.length && learnedWords(student.words) !== 0,
            'is-false': learnedWords(student.words) !== student.words.length
          }">{{ learnedWords(student.words) }}</td>
          </tr>
        </tbody>
      </table>
      
      <h4>Students</h4>

      <ul>
        <li v-for="student in group.students">
          <div>
            {{ student.username }}
            <router-link
              class="button"
              :to="'/groups/' + group.group_id + '/' + student.student_id"
              >View Details</router-link
            >
            <StudentDetails
              :show="showStudentDetails"
              :student="studentDetails"
              @cancel="cancelStudentDetails"
            />
          </div>
          <br />
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
      showTable: false,
    };
  },
  mounted() {
    const formData = {
      group_id: this.$route.params.id,
    };
    this.$store.dispatch("fetchGroup", formData);
  },
  computed: {
    group() {
      return this.$store.state.group;
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
    completedTrainings(words) {
      return words.reduce((count, word) => {
        let completedCount = 0;
        if (word.cards) completedCount++;
        if (word.word_translation) completedCount++;
        if (word.constructor) completedCount++;
        if (word.word_audio) completedCount++;
        return count + completedCount;
      }, 0);
    },
    learnedWords(words) {
      return words.reduce((count, word) => {
        let completedCount = 0;
        if (word.is_learned) completedCount++;
        return count + completedCount;
      }, 0);
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

table {
  width: 100%;
  border: 1px solid #ddd;
}

th,
td {
  padding: 8px;
  border: 1px solid #ddd;
  text-align: left;
}

th {
  background-color: #f0f0f0;
  font-weight: bold;
}

tbody tr:nth-child(odd) {
  background-color: #fff;
}

tbody tr:nth-child(even) {
  background-color: #f5f5f5;
}

.is-true {
  background-color: lightgreen;
}

.is-false {
  background-color: lightcoral;
}
</style>
