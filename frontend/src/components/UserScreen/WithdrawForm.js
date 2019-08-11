import React from 'react'
import { Field, reduxForm } from 'redux-form'
import Style from 'styled-components'

const WithdrawForm = ({ handleSubmit, pristine, submitting }) => {
  return (
    <Wrapper onSubmit={handleSubmit}>
      <FieldWrapper>
        <Field
          name="amount"
          component={renderField}
          type="text"
          placeholder="Amount"
          validate={validations}
        />
      </FieldWrapper>
      <Submit type="submit" disabled={pristine || submitting}>
        Get
      </Submit>
    </Wrapper>
  )
}

const validations = [
    value => (value && isNaN(Number(value)) ? 'Must be positive integer' : undefined),
    value => (value && value < 0 ? 'Must be positive integer' : undefined),
    value => (value && value.indexOf(',') !== -1 ? 'Must be positive integer' : undefined),
    value => (value && value.indexOf('.') !== -1 ? 'Must be positive integer' : undefined),
]


const renderField = ({
  input,
  label,
  type,
  meta: { touched, error, warning }
}) => (
  <div>
    <FieldWrapper>
      <input {...input} placeholder={label} type={type} />
      {touched &&
        ((error && <span className='form-err-msg'>{error}</span>))}
    </FieldWrapper>
  </div>
)

export default reduxForm({
  form: 'withdrawForm'
})(WithdrawForm)

const Wrapper = Style.form`
    text-align: center;
    place-self: start center;
`

const FieldWrapper = Style.div`
    position: relative;
    
    input {
        border: none;
        border-radius: 10px;
        width: 130px;
        height: 35px;
        color: var(--accent);
        text-align: end;
        font-size: 20px;
        font-weight: 700;
        padding-right: 10px;
    }
    
    span {
        display: block;
        position: absolute;
        width: 100%;
        margin-top: 5px;
        border: 1px solid white;
    }
    
    input:focus {
        outline: 0;
    }
`

const Submit = Style.button`
    margin-top: 60px;
    color: white;
    background-color: var(--accent);
    border: none;
    border-radius: 10px;
    font-size: 20px;
    font-weight: 600;
    padding: 7px 15px;
    
    :focus {
        outline: 0;
    }
        
    :disabled {
        background-color: var(--accent-disabled);
    }
`

