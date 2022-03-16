<template>
    <form @submit="onSubmit" class="form-inline">
        <input 
            type="number"
            name="site-id"
            v-model="id"
            placeholder="AUDATEX_SITE_ID" 
        />
        <input 
            type="text"
            name="site-id"
            v-model="garageName"
            placeholder="GARAGE_NAME"
        />
        <input 
            type="text"
            name="approval-type"
            v-model="approvalType"
            placeholder="APPROVAL_TYPE"
        />
        <input 
            type="text"
            name="approval-subtype"
            v-model="approvalSubType"
            placeholder="APPROVAL_SUBTYPE"
        />
        <input 
            type="date"
            name="start-date"
            v-model="startDate"
            placeholder="START_DATE"
        />
        <input 
            type="date"
            name="end-date"
            v-model="endDate"
            placeholder="END_DATE"
        />
        <button type="submit" value="Save New Row" class="pure-button">
            Save New Row
        </button>
    </form>
</template>

<script>
export default {
    name: 'NewRow',
    data () {
        return {
            uuid: '',
            id: '',
            garageName: '',
            approvalType: '',
            approvalSubType: '',
            startDate: '',
            endDate: ''
        }
    },
    methods: {
        onSubmit (e) {
            e.preventDefault()

            if(!this.id) {
                alert('Make sure to enter a site id!')
                return
            }

            const newRow = {
                uuid: crypto.randomUUID(),
                id: this.id,
                garageName: this.garageName,
                approvalType: this.approvalType,
                approvalSubType: this.approvalSubType,
                startDate: this.startDate,
                endDate: this.endDate
            }

            this.$emit('submit-new-row', newRow)
        }
    }
}
</script>

<style>
/* Style the form - display items horizontally */
.form-inline {
    width: 100%;
    margin-left: auto;
    margin-right: auto;
}

/* Add some margins for each label */
.form-inline label {
    margin: 5px 10px 5px 0;
}

/* Style the input fields */
.form-inline input {
    width: auto;
    vertical-align: middle;
    margin: 5px 10px 5px 0;
    padding: 10px;
    background-color: #fff;
    border: 1px solid #ddd;
}

/* Style the submit button */
.form-inline button {
    padding: 10px 20px;
    background-color: dodgerblue;
    border: 1px solid #ddd;
    color: white;
}

.form-inline button:hover {
    background-color: royalblue;
}
</style>