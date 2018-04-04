package ie.sdn.dto;

import ie.sdn.model.UserToken;

public class UserTokenDTO {
    private String id;
    private String token;
    private String userId;
    private String status;

    public UserTokenDTO() {
    }

    public UserTokenDTO(UserToken userToken) {
        this.id = userToken.getId();
        this.token = userToken.getToken();
        this.userId = userToken.getUserId();
        this.status = userToken.getStatus();
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }

    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
}
