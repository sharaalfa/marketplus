package sharafutdinov.artur.marketplus.dao;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.orm.hibernate4.HibernateTemplate;
import org.springframework.stereotype.Service;
import sharafutdinov.artur.marketplus.model.Role;

import java.io.Serializable;
import java.util.List;

/**
 * Created by first on 21.03.17.
 */
@Service
public class RoleDAO implements GenericDao<Role,Integer>{

    @Autowired
    private HibernateTemplate hibernateTemplate;

    @Override
    public Role load(final Integer id) {
        return hibernateTemplate.load(Role.class,id);
    }

    @Override
    public Role get(final Integer id) {
        return hibernateTemplate.get(Role.class,id);
    }

    @Override
    public List<Role> getAll() {
        return hibernateTemplate.loadAll(Role.class);
    }

    @Override
    public Serializable save(final Role object) {
        return hibernateTemplate.save(object);
    }

    @Override
    public void saveOrUpdate(final Role object) {
        hibernateTemplate.saveOrUpdate(object);
    }

    @Override
    public void delete(final Role object) {
        hibernateTemplate.delete(object);
    }

    @Override
    public Long count() {
        return new Long(hibernateTemplate.loadAll(Role.class).size());
    }

    @Override
    public void flush() {
        hibernateTemplate.flush();
    }
}
