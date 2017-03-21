/*package sharafutdinov.artur.marketplus.model;

import javax.persistence.*;

/**
 * Created by first on 21.03.17.
 */
/*@Entity
@Table(name = "USER_ROLE", schema = "public", catalog = "marketplusdb")
@IdClass(UserRoleEntityPK.class)
public class UserRoleEntity {
    private String userId;
    private int roleId;

    @Id
    @Column(name = "user_id")
    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }

    @Id
    @Column(name = "role_id")
    public int getRoleId() {
        return roleId;
    }

    public void setRoleId(int roleId) {
        this.roleId = roleId;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        UserRoleEntity that = (UserRoleEntity) o;

        if (roleId != that.roleId) return false;
        if (userId != null ? !userId.equals(that.userId) : that.userId != null) return false;

        return true;
    }

    @Override
    public int hashCode() {
        int result = userId != null ? userId.hashCode() : 0;
        result = 31 * result + roleId;
        return result;
    }
}
*/