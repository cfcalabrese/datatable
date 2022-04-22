<template>
    <div class="border-b border-x rounded-lg border-slate-800 w-full mb-1">
        <h1 class="ml-2 text-lg text-white font-bold tracking-wider">Filters</h1>
    </div>
    <div class="grid gap-2 grid-cols-4 text-right">
        <div class="pb-1">
            <DropDownUniqueListItem
                :uniqueVals="distinctIds"
                @filter="setIdFilterValue"
                text="AUDATEX_SITE_ID"
                id="siteid" 
            />       
        </div>
        <div class="pb-1">
            <DropDownUniqueListItem
                :uniqueVals="distinctGarageNames"
                @filter="setGarageNameFilterValue"
                text="GARAGE_NAME"
                id="garagename"
            />        
        </div>
        <div class="pb-1">
            <DropDownUniqueListItem
                :uniqueVals="distinctTypes"
                @filter="setTypeFilterValue"
                text="APPROVAL_TYPE"
                id="type"
            />        
        </div>
        <div class="pb-1">
            <DropDownUniqueListItem
                :uniqueVals="distinctSubTypes"
                @filter="setSubTypeFilterValue"
                text="APPROVAL_SUBTYPE"
                id="subtype"
            />        
        </div>
    </div>
    <table class="overflow-hidden rounded-t min-w-full drop-shadow-xl table-auto">
        <thead class='bg-slate-700 text-sm text-right text-slate-400 tracking-wider'>
            <tr>
                <th class="py-2 px-2">AUDATEX_SITE_ID</th>
                <th>GARAGE_NAME</th>
                <th>APPROVAL_TYPE</th>
                <th>APPROVAL_SUBTYPE</th>
                <th>START_DATE</th>
                <th>END_DATE</th>
                <th class="px-2"></th>
                <th class="px-2"></th>
            </tr>
        </thead>
        <tbody class='bg-slate-800 text-white text-bold'>
            <ApprovalItem
                :key="approval.UUID" v-for="approval in dataPaginated"
                :Approval="approval" 
                @delete-row="deleteRow"
                @edit-row="editRow"
            />
        </tbody>
    </table>
    <PageChangerItem 
        :pageNumber="pageNum"
        @change-page="incrementPageNum"
    />
    <NewRow @submit-new-row="addRow" v-show="showAddRow" />
    <NewRowButton 
        @btn-click="toggleAddRow" 
        :text="showAddRow ? 'Close' : 'Add New Row'"
        class="mt-2"
    />
</template>

<script>
import ApprovalItem from './ApprovalItem'
import NewRow from './NewRow'
import NewRowButton from './NewRowButton'
import DropDownUniqueListItem from './DropDownUniqueListItem'
import PageChangerItem from './PageChangerItem.vue'

export default {
    name: 'ApprovalsList',
    components: {
        ApprovalItem,
        NewRow,
        NewRowButton,
        DropDownUniqueListItem,
        PageChangerItem
    },
    data () {
        return {
            showAddRow: false,
            approvals: [],
            editedRow: this.editedRow,
            idFilterValue: '',
            garageNameFilterValue: '',
            typeFilterValue: '',
            subTypeFilterValue: '',
            startFilterValue: '',
            endFilterValue: '',
            rowsPerPage: 10,
            pageNum: 1
        }
    },
    methods: {
        incrementPageNum (increment) {
            let newPageNum = this.pageNum + increment
            if (newPageNum < 1) {
                this.pageNum = 1 
            } else if (newPageNum > this.numPages) {
                this.pageNum = this.numPages
            } else {
                this.pageNum = newPageNum
            }
        },
        setIdFilterValue (uniqueVal) {
            this.idFilterValue = uniqueVal
        },
        setGarageNameFilterValue (uniqueVal) {
            this.garageNameFilterValue = uniqueVal
        },
        setTypeFilterValue (uniqueVal) {
            this.typeFilterValue = uniqueVal
        },
        setSubTypeFilterValue (uniqueVal) {
            this.subTypeFilterValue = uniqueVal
        },
        getIdFilterValue (val) {
            this.idFilterValue = val
        },
        getGarageNameFilterValue (val) {
            this.garageNameFilterValue = val
        },
        getTypeFilterValue (val) {
            this.typeFilterValue = val
        },
        getSubTypeFilterValue (val) {
            this.subTypeFilterValue = val
        },
        getStartFilterValue (val) {
            this.startFilterValue = val
        },
        getEndFilterValue (val) {
            this.endFilterValue = val
        },
        toggleAddRow () {
            this.showAddRow = !this.showAddRow
        },
        async addRow (newRow) {
            const res = await fetch('api/v1/data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    "UUID": newRow.uuid,
                    "AUDATEX_SITE_ID": newRow.id,
                    "GARAGE_NAME": newRow.garageName,
                    "APPROVAL_TYPE": newRow.approvalType,
                    "APPROVAL_SUBTYPE": newRow.approvalSubType,
                    "START_DATE": newRow.startDate,
                    "END_DATE": newRow.endDate
                })
            })

            this.approvals = [...this.approvals, await this.fetchApproval(newRow.uuid)]
        },
        async fetchApprovals () {
            const res = await fetch('api/v1/data')

            const data = await res.json()

            return data.approvals
        },
        async deleteRow (uuid) {
            if(confirm('Are you sure you want to delete this row?')) {
                const res = await fetch(`api/v1/data/${uuid}`, {
                    method: 'DELETE'
                })
                res.status === 200 ? (this.approvals = this.approvals.filter((approval) => 
                    (approval.UUID !== uuid)
                )) : alert('Error deleting task')
            }
        },
        async deleteRow (uuid) {
            if(confirm('Are you sure you want to delete this row?')) {
                const res = await fetch(`api/v1/data/${uuid}`, {
                    method: 'DELETE'
                })
                res.status === 200 ? (this.approvals = this.approvals.filter((approval) => 
                    (approval.UUID !== uuid)
                )) : alert('Error deleting task')
            }
        },
        async editRow (editedRow) {        
            const res = await fetch(`api/v1/data/${editedRow.uuid}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    'UUID': editedRow.uuid,
                    'AUDATEX_SITE_ID': editedRow.id,
                    'GARAGE_NAME': editedRow.garageName,
                    'APPROVAL_TYPE': editedRow.approvalType,
                    'APPROVAL_SUBTYPE': editedRow.approvalSubType,
                    'START_DATE': editedRow.startDate,
                    'END_DATE': editedRow.endDate
                })
            })
            this.approvals.map((approval) => {
                if (approval.UUID === editedRow.uuid) {
                    approval.AUDATEX_SITE_ID = editedRow.id,
                    approval.GARAGE_NAME = editedRow.garageName,
                    approval.APPROVAL_TYPE = editedRow.approvalType,
                    approval.APPROVAL_SUBTYPE = editedRow.approvalSubType,
                    approval.START_DATE = editedRow.startDate,
                    approval.END_DATE = editedRow.endDate
                }
            })
            console.log(this.approvals)
        },
        async fetchApproval (uuid) {
            const res = await fetch(`api/v1/data/${uuid}`)

            const data = await res.json()

            return data.approval
        }
    },
    async created () {
        this.approvals = await this.fetchApprovals()
    },
    computed: {
        numPages () {
            let perPage = this.rowsPerPage
            let numPages = Math.ceil(this.filteredApprovals.length / perPage)
            return numPages
        },
        dataPaginated () {
            let perPage = this.rowsPerPage
            let pageNum = this.pageNum
            let dataPaginated = this.filteredApprovals.filter((a, index) => {
                return (
                    index > ((pageNum - 1) * perPage) - 1 &&
                    index < pageNum * perPage
                )
            })

            return dataPaginated
        },
        filteredApprovals () {
            let filteredApprovals = this.approvals.filter((a) => {
                return (
                    a.AUDATEX_SITE_ID.toString().includes(this.idFilterValue) &&
                    a.GARAGE_NAME.includes(this.garageNameFilterValue) &&
                    String(a.APPROVAL_TYPE).includes(this.typeFilterValue) &&
                    String(a.APPROVAL_SUBTYPE).includes(this.subTypeFilterValue)
                )
            })

            return filteredApprovals
        },
        distinctIds () {
            let distinctIds = [
                ...new Set(this.filteredApprovals.map(
                    approval => approval.AUDATEX_SITE_ID
                ))
            ]
            return distinctIds
        },
        distinctGarageNames () {
            let distinctGarageNames = [
                ...new Set(this.filteredApprovals.map(
                    approval => approval.GARAGE_NAME
                ))
            ]
            return distinctGarageNames
        },
        distinctTypes () {
            let distinctTypes = [
                ...new Set(this.filteredApprovals.map(
                    approval => approval.APPROVAL_TYPE
                ))
            ]
            return distinctTypes
        },
        distinctSubTypes () {
            let distinctSubTypes = [
                ...new Set(this.filteredApprovals.map(
                    approval => approval.APPROVAL_SUBTYPE
                ))
            ]
            return distinctSubTypes
        }
    },
    emits: ['delete-row', 'edit-row']
}
</script>
