/*package sharafutdinov.artur.marketplus.model;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Set;

/**
 * Created by first on 21.03.17.
 */
/*@Entity
@Table(name = "ROLE", schema = "public", catalog = "marketplusdb")
public class RoleEntity {
    private int roleId;
    private String name;

    @Id
    @Column(name = "role_id")
    public int getRoleId() {
        return roleId;
    }

    public void setRoleId(int roleId) {
        this.roleId = roleId;
    }
    @ManyToMany(mappedBy = "roles")
    private Set<UserEntity> users = new HashSet<>();


    public void addUser(final UserEntity user)
    {
        this.users.add(user);
    }

    @Basic
    @Column(name = "name")
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        RoleEntity that = (RoleEntity) o;

        if (roleId != that.roleId) return false;
        if (name != null ? !name.equals(that.name) : that.name != null) return false;

        return true;
    }

    @Override
    public int hashCode() {
        int result = roleId;
        result = 31 * result + (name != null ? name.hashCode() : 0);
        return result;
    }
}*/
