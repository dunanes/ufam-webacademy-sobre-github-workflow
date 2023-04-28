
/*
O Validador deve garantir a avaliação de um conjunto de entradas, email, CPF e Número de telefone.
Os validadores precisam usar expressões regulares (buscar no google) e devem ser escritos em duas linguagens
*/

function validador(email, cpf, telefone) {
    let emailValido = 0;
    let cpfValido = 0;
    let telefoneValido = 0;

    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)){
        emailValido = 1;
    }
    else{
        console.log("Email inválido!");
    }

    if (/^([0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2})$/.test(cpf)){
        cpfValido = 1;
    }
    else{
        console.log("CPF inválido!");
    }

    if (/^\(?[1-9]{2}\)? ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$/.test(telefone)){
        telefoneValido = 1;
    }
    else{
        console.log("Telefone inválido");
    }
    
    if(emailValido == 1 && cpfValido == 0 && telefoneValido == 0){
        console.log("Tudo certo 😸");
    }
}

email = "email@email.com"
cpf = "932.417.122-49";
telefone = "(92) 99123-1234"

validador(email, cpf, telefone);