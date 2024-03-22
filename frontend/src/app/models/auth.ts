export type AccessTokenType = {
    access_token: string,
    token_type: string
}
  
export type isAuthResponseType = {
    user: {
        username: string,
        user_id: number,
    }
}

export type UserInfoType = {
    username: string
}

export type TypeRegisterForm = {
    username: string,
    password: string,
}