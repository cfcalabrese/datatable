<template>
  <div class="container">
    <DataTable/>
    <br>
    <!-- <SubmitButton /> -->
  </div>
</template>

<script>
// @ is an alias to /src
import DataTable from '@/components/DataTable'
import NewRowButton from '../components/NewRowButton'
import SubmitButton from '../components/SubmitButton'
import NewRow from '../components/NewRow'

export default {
  name: 'HomeView',
  data () {
    return {
      showAddRow: false
    }
  },
  components: {
    DataTable,
    NewRowButton,
    SubmitButton,
    NewRow
  },
  methods: {
    toggleAddRow () {
      this.showAddRow = !this.showAddRow
    }
  }
}
</script>
