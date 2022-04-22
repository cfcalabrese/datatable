<template>
  <div class="rounded-lg m-6">
    <DataTable/>
    <br>
  </div>
</template>

<script>
// @ is an alias to /src
import DataTable from '@/components/DataTable'
import ButtonItem from '@/components/ButtonItem'
import NewRow from '@/components/NewRow'

export default {
  name: 'HomeView',
  data () {
    return {
      showAddRow: false
    }
  },
  components: {
    DataTable,
    ButtonItem,
    NewRow
  },
  methods: {
    toggleAddRow () {
      this.showAddRow = !this.showAddRow
    }
  }
}
</script>
