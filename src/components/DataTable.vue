<template>
    <div class="content">
        <table class="pure-table pure-table-horizontal center">
            <thead>
                <tr>
                    <th>AUDATEX_SITE_ID</th>
                    <th>GARAGE_NAME</th>
                    <th>APPROVAL_TYPE</th>
                    <th>APPROVAL_SUBTYPE</th>
                    <th>START_DATE</th>
                    <th>END_DATE</th>
                    <th></th>
                    <th></th>
                </tr>
            </thead>
            <ApprovalsList 
                :Approvals="approvals" 
                @delete-row="deleteRow"
                @edit-row="editRow"
            />
        </table>
        <div v-show="showAddRow" class="center content">
            <NewRow @submit-new-row="addRow"/>
        </div>
        <NewRowButton 
            @btn-click="toggleAddRow" 
            :text="showAddRow ? 'Close' : 'Add New Row'"
        />
    </div>
</template>

<script>
import NewRow from './NewRow'
import NewRowButton from './NewRowButton'
import ApprovalsList from './ApprovalsList'

export default {
    name: 'DataTable',
    components:{
        NewRow,
        NewRowButton,
        ApprovalsList
    },
    data () {
        return {
            showAddRow: false,
            approvals: [],
            editedRow: this.editedRow
        }
    },
    methods: {
        toggleAddRow () {
            this.showAddRow = !this.showAddRow
        },
        addRow (newRow) {
            this.approvals = [...this.approvals, newRow]
        },
        deleteRow (uuid) {
            if(confirm('Are you sure you want to delete this row?')) {
                this.approvals = this.approvals.filter((approval) => 
                    (approval.uuid !== uuid)
                )
            }
        },
        editRow (editedRow) {           
            this.approvals.map((approval) => {
                if (approval.uuid === editedRow.uuid) {
                    approval.id = editedRow.id,
                    approval.garageName = editedRow.garageName,
                    approval.approvalType = editedRow.approvalType,
                    approval.approvalSubType = editedRow.approvalSubType,
                    approval.startDate = editedRow.startDate,
                    approval.endDate = editedRow.endDate
                }
            })

            console.log(this.approvals)

            //     )
            // )

        }
    },
    created () {
        this.approvals = [
            {
                uuid: crypto.randomUUID(),
                id: 1,
                garageName: "dave's",
                approvalType: "NARG",
                approvalSubType: "S & SE",
                startDate: "2021-01-01",
                endDate: "2022-01-01"
            },
            {
                uuid: crypto.randomUUID(),
                id: 2,
                garageName: "hazel's",
                approvalType: "AVANT",
                approvalSubType: null,
                startDate: "2020-01-01",
                endDate: null
            }
        ]
    }
}
</script>

<style>
    .center {
        margin-left: auto;
        margin-right: auto;
        width: 100%;
    }
</style>