import React from 'react'
import { Field, reduxForm } from 'redux-form'
import Style from 'styled-components'
export const fieldNames = {
  TWENTY_THOUSAND: 'TWENTY_THOUSAND',
  TEN_THOUSAND: 'TEN_THOUSAND',
  FIVE_THOUSAND: 'FIVE_THOUSAND',
  TWO_THOUSAND: 'TWO_THOUSAND'
}

const FillBillForm = ({ handleSubmit, pristine, submitting }) => {
  return (
    <Wrapper onSubmit={handleSubmit}>
      <FieldWrapper>
        <Field
          name={fieldNames.TWENTY_THOUSAND}
          component={renderField}
          type="text"
          validate={validations}
        />
      </FieldWrapper>
      <FieldWrapper>
        <Field
          name={fieldNames.TEN_THOUSAND}
          component={renderField}
          type="text"
          validate={validations}
        />
      </FieldWrapper>
      <FieldWrapper>
        <Field
          name={fieldNames.FIVE_THOUSAND}
          component={renderField}
          type="text"
          validate={validations}
        />
      </FieldWrapper>
      <FieldWrapper>
        <Field
          name={fieldNames.TWO_THOUSAND}
          component={renderField}
          type="text"
          validate={validations}
        />
      </FieldWrapper>
      <Submit type="submit" disabled={pristine || submitting}>
        Fill
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
    <div>
      <input {...input} placeholder={label} type={type} />
      {touched &&
        ((error && <Error className="form-err-msg">{error}</Error>))}
    </div>
  </div>
)

export default reduxForm({
  form: 'fillBillForm'
})(FillBillForm)


const Wrapper = Style.form`
    display: grid;
    
    place-items: center;
    grid-template-columns: repeat(4, 1fr);
    width: 85%;
    margin: 0 auto;
    margin-top: 5px;
    
`

const FieldWrapper = Style.div`
    position: relative;
    
    input {
        border: none;
        border-radius: 7px;
        width: 60px;
        height: 25px;
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
    margin-top: 55px;
    margin-right: -280px;
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

const Error = Style.span`
    font-size: 10px;
    font-weight: 600;
`
